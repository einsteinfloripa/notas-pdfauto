import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
#import createpdf
planilhabruta = 'respostabruta.csv'
planilhagabarito = 'gabarito.csv'
df = pd.read_csv(planilhabruta)
gabarito = pd.read_csv(planilhagabarito)

n_linhas = df.shape[0]
n_colunas = df.shape[1]

# df.iloc[0,1] pega a linha0 e coluna 1
# nome é coluna 0
print(df.columns[62]) #- exibe o nome da coluna 62
pdf_pages = PdfPages("todos_os_graficos.pdf")  # Cria um objeto PDF
#gabarito iloc[0,0] => anulada




for coluna in range(3,63): #vamos pegar a coluna da questão 1 e ir até a coluna da questão 62
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for linha in range(n_linhas):
        colunaG = coluna-3
        gabaritoC = gabarito.iloc[colunaG,0]
        resposta_aluno = df.iloc[linha,coluna]
        if resposta_aluno=="A":
            a= a + 1
        elif resposta_aluno=="B":
            b = b + 1
        elif resposta_aluno=="C":
            c = c + 1
        elif resposta_aluno=='D':
            d = d + 1
        elif resposta_aluno=="E":
            e = e + 1
        elif resposta_aluno=='NAO DETECTADO':
            continue
    data = {
        'a':a,
        'b':b,
        'c':c,
        'd':d,
        'e':e,
    }
    print(a,b,c,d,e)
    courses = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon', 
            width = 0.4)
    
    plt.xlabel(f"ALTERNATIVAS - Resposta correta: {gabaritoC}")
    plt.ylabel(f"Quantidade de vezes assinalada")
    plt.title(f"Distribuição de respostas. Questão: {coluna-2}")
    # Salvar o gráfico em um arquivo PDF
    pdf_pages.savefig(fig)
    plt.close()  # Fechar a figura para liberar a memória
pdf_pages.close()  # Fecha o objeto PDFs