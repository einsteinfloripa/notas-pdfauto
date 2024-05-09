import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
#import createpdf
planilhabruta = 'dados_corrigidos - SIMULINHO 2024 - dados_corrigidos (1).csv'
planilhagabarito = 'Gabarito Simulinho 2024 - vale - Página1 (1).csv'
df = pd.read_csv(planilhabruta)



gabarito = pd.read_csv(planilhagabarito)



n_linhas = df.shape[0]
n_colunas = df.shape[1]

pdf_pages = PdfPages("vni.pdf")  # Cria um objeto PDF
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

mediaDeAcertos = {
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

textCorrector = {
    'matematica': 'Matemática',
    'portugues': 'Português',
    'fisica': 'Física',
    'quimica': 'Química',
    'historia': 'História',
    'biologia': 'Biologia', #Na planilha ta invertido. A questão 41 na planilha é Biologia,quando
    'geografia': 'Geografia', #na verdade na prova a quest 41 é Geografia
    'ingles': 'Inglês',
    'interdisciplinar': 'Interdisciplinar',
    'filosofia-sociologia': 'Filosofia-Sociologia'  
}

fig_count = 0  # Contador de figuras por página
for coluna in range(3, 53):
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
    questaoStr = questoes_em_porcentagem
    data_per[f'Questão {questaoStr}'] = coluna
    data = {
        f'A|{a}': a,
        f'B|{b}': b,
        f'C|{c}': c,
        f'D|{d}': d,
        f'E|{e}': e,
    }

    print(f'Questão:{coluna-2} Disciplina:{disciplina} Gabarito: {gabaritoC}\n A: {a}\n B: {b}\n C: {c}\n D: {d}\n E: {e} ')
    print(erraram, acertaram)
    courses = list(data.keys())
    values = list(data.values())
    
    if fig_count == 0:
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # Duas figuras por página
        fig_count = 0

    # Criando o gráfico de barras
    # Criando o gráfico de barras
    axs[fig_count].bar(courses, values, color=textColor[disciplina], width=0.4)
    axs[fig_count].set_xlabel(f"Resposta correta: {gabaritoC}", fontsize=11)
    axs[fig_count].set_ylabel(f"Quantidade de vezes assinalada", fontsize=10)
    axs[fig_count].set_title(f"Questão: {coluna-2} Disciplina: {textCorrector[disciplina]}", fontsize=11)
    if gabaritoC != 'Anulada':
        axs[fig_count].text(0.52, 1.06, f" Erraram: {erraram}% | Acertaram: {acertaram}% ", ha='center', transform=axs[fig_count].transAxes, fontsize=11)

    # Definindo a escala do eixo y entre 5 e 80
    axs[fig_count].set_ylim(5, 80)

    
    fig_count += 1
    if fig_count == 2:
        pdf_pages.savefig(fig)
        plt.close(fig)
        fig_count = 0

if fig_count != 0:
    pdf_pages.savefig(fig)
    plt.close(fig)

pdf_pages.close()

#createpdf.tableNotes(data_per)