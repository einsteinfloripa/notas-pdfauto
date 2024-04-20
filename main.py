import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import createpdf
planilhabruta = 'respostabruta.csv'
planilhagabarito = 'gabarito.csv'
df = pd.read_csv(planilhabruta)
gabarito = pd.read_csv(planilhagabarito)

n_linhas = df.shape[0]
n_colunas = df.shape[1]

pdf_pages = PdfPages("sera.pdf")  # Cria um objeto PDF
data_per = {}
textColor = {
    'matematica': 'green',
    'portugues': '#B8AA5E',
    'fisica': 'red',
    'quimica': 'blue',
    'historia': 'orange',
    'biologia': 'purple',
    'geografia': 'cyan',
    'ingles': 'pink',
    'interdisciplinar': 'brown',
    'filosofia-sociologia': 'gray'  
}

fig_count = 0  # Contador de figuras por página
for coluna in range(3, 63):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    acertaram = 0
    erraram = 0
    for linha in range(n_linhas - 1):
        colunaG = coluna - 3
        disciplina = df.iloc[0, coluna]
        gabaritoC = gabarito.iloc[colunaG, 0]
        resposta_aluno = df.iloc[linha, coluna]
        if resposta_aluno == 'NAO DETECTADO':
            continue
        if resposta_aluno == "A":
            a += 1
        elif resposta_aluno == "B":
            b += 1
        elif resposta_aluno == "C":
            c += 1
        elif resposta_aluno == 'D':
            d += 1
        elif resposta_aluno == "E":
            e += 1
        if resposta_aluno == gabaritoC:
            acertaram += 1
        else:
            erraram += 1

    total_respostas = acertaram + erraram
    acertaram = (acertaram / total_respostas) * 100
    erraram = (erraram / total_respostas) * 100
    acertaram = f'{acertaram:.1f}'
    erraram = f'{erraram:.1f}'
    questoes_em_porcentagem = {
        'discplina':disciplina,
        'erros':erraram,
        'acertos':acertaram
    }
    quest = f'Questão{coluna-2}'
    data_per[f'{quest}{questoes_em_porcentagem}'] = questoes_em_porcentagem
    data = {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
    }

    # print(f'Gabarito: {gabaritoC}\n A: {a}\n B: {b}\n C: {c}\n D: {d}\n E: {e}')
    # print(erraram, acertaram)
    courses = list(data.keys())
    values = list(data.values())
    
    if fig_count == 0:
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # Duas figuras por página
        fig_count = 0

    # Criando o gráfico de barras
    axs[fig_count].bar(courses, values, color=textColor[disciplina], width=0.4)
    axs[fig_count].set_xlabel(f"Resposta correta: {gabaritoC}", fontsize=8)
    axs[fig_count].set_ylabel(f"Quantidade de vezes assinalada", fontsize=8)
    axs[fig_count].set_title(f"Distribuição de respostas - Questão: {coluna-2} Disciplina: {disciplina}", fontsize=8)
    if gabaritoC != 'Anulada':
        axs[fig_count].text(0.92, 1.02, f"| Erraram: {erraram}% - Acertaram: {acertaram}% |", ha='center', transform=axs[fig_count].transAxes, fontsize=8)
    
    fig_count += 1
    if fig_count == 2:
        pdf_pages.savefig(fig)
        plt.close(fig)
        fig_count = 0

if fig_count != 0:
    pdf_pages.savefig(fig)
    plt.close(fig)

pdf_pages.close()

print(data_per['Questão1'][disciplina])


#reatepdf.tableNotes(data_per)


