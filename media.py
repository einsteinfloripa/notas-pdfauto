import pandas as pd
import matplotlib.pyplot as plt

dados_brutos = pd.read_csv('ranking_alunos.xlsx', dtype="str")
disciplina_media_qntdade = {
        'matematica':0,
        "portugues":0,
        "quimica":0,
        "historia":0,
        "geografia":0,
        "fisica":0,
        "biologia":0,
        "filosofia-sociologia":0
}

disciplina_cor = {
    'matematica':'#7F7F7F',
    "portugues":'#FE7F0E',
    "quimica":'#8C564A',
    "historia":'#D52728',
    "geografia":'#1F78B4',
    "fisica":'#E576C2',
    "biologia":'#9467BC',
    "filosofia-sociologia":'#2BA02D'
}

def quantidadeMediaGeral(): #Média geral
    linhas = dados_brutos.shape[0]
    for coluna in range(2,10):
        disciplina = dados_brutos.iloc[0,coluna]
        total = 0
        for linha in range(1,linhas):
            valor = int(dados_brutos.iloc[linha,coluna])
            total = valor + total
        media = f'{total/96:.1f}'
        disciplina_media_qntdade[disciplina] = media
    print('Quantidade Média de questões acertadas por Disciplina')
    for nota in disciplina_media_qntdade:
        print(f'{nota}:{disciplina_media_qntdade[nota]}')
    disciplina_media_qntdade_ordenado = dict(sorted(disciplina_media_qntdade.items(), key=lambda item: item[1]))
    disciplinas = list(disciplina_media_qntdade_ordenado.keys())
    medias = list(disciplina_media_qntdade_ordenado.values())
    plt.figure(figsize=(12, 6))
    cores = [disciplina_cor[disciplina] for disciplina in disciplinas]
    plt.bar(disciplinas, medias, color=cores,width=0.3)
    plt.xlabel('Disciplinas')
    plt.ylabel('Médias')
    plt.title('Quantidade Média de questões acertadas por Disciplina')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('quantidadeMediaGeral')
quantidadeMediaGeral()
disciplina_media_qntdade = {
        'matematica':0,
        "portugues":0,
        "quimica":0,
        "historia":0,
        "geografia":0,
        "fisica":0,
        "biologia":0,
        "filosofia-sociologia":0
}
def quantidadeMediaPercentilUP(): #PERCENTIL 85 - Pegando as 15 melhores notas
    linhas = dados_brutos.shape[0]
    for coluna in range(2,10):
        disciplina = dados_brutos.iloc[0,coluna]
        total = 0
        for linha in range(1,16):
            valor = int(dados_brutos.iloc[linha,coluna])
            total = valor + total
        media = f'{total/16:.1f}'
        disciplina_media_qntdade[disciplina] = media
    print('Quantidade Média de questões acertadas por Disciplina')
    for nota in disciplina_media_qntdade:
        print(f'{nota}:{disciplina_media_qntdade[nota]}')
    disciplina_media_qntdade_ordenado = dict(sorted(disciplina_media_qntdade.items(), key=lambda item: item[1]))
    disciplinas = list(disciplina_media_qntdade_ordenado.keys())
    medias = list(disciplina_media_qntdade_ordenado.values())
    plt.figure(figsize=(12, 6))
    cores = [disciplina_cor[disciplina] for disciplina in disciplinas]
    plt.bar(disciplinas, medias, color=cores,width=0.3)
    plt.xlabel('Disciplinas')
    plt.ylabel('Médias')
    plt.title('Quantidade Média de questões acertadas por Disciplina')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('quantidadeMediaPercentilUP')
quantidadeMediaPercentilUP()
disciplina_media_qntdade = {
        'matematica':0,
        "portugues":0,
        "quimica":0,
        "historia":0,
        "geografia":0,
        "fisica":0,
        "biologia":0,
        "filosofia-sociologia":0
}
def quantidadeMediaPercentilDOWN(): #Pegando as 15 piores notas
    linhas = dados_brutos.shape[0]
    for coluna in range(2,10):
        disciplina = dados_brutos.iloc[0,coluna]
        total = 0
        for linha in range(81,linhas):
            valor = int(dados_brutos.iloc[linha,coluna])
            total = valor + total
        media = f'{total/15:.1f}'
        disciplina_media_qntdade[disciplina] = media
    print('Quantidade Média de questões acertadas por Disciplina')
    for nota in disciplina_media_qntdade:
        print(f'{nota}:{disciplina_media_qntdade[nota]}')
    disciplina_media_qntdade_ordenado = dict(sorted(disciplina_media_qntdade.items(), key=lambda item: item[1]))
    disciplinas = list(disciplina_media_qntdade_ordenado.keys())
    medias = list(disciplina_media_qntdade_ordenado.values())
    plt.figure(figsize=(12, 6))
    cores = [disciplina_cor[disciplina] for disciplina in disciplinas]
    plt.bar(disciplinas, medias, color=cores,width=0.3)
    plt.xlabel('Disciplinas')
    plt.ylabel('Médias')
    plt.title('Quantidade Média de questões acertadas por Disciplina')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('quantidadeMediaPercentilDOWN')
quantidadeMediaPercentilDOWN()
disciplina_media_qntdade = {
        'matematica':0,
        "portugues":0,
        "quimica":0,
        "historia":0,
        "geografia":0,
        "fisica":0,
        "biologia":0,
        "filosofia-sociologia":0
}
def quantidadeMediaPercentilREGULAR(): #Média geral dos estudantes que estão entre os 15 primeiros
    linhas = dados_brutos.shape[0]     #E 15 ultimos 
    for coluna in range(2,10):
        disciplina = dados_brutos.iloc[0,coluna]
        total = 0
        for linha in range(17,81):
            valor = int(dados_brutos.iloc[linha,coluna])
            total = valor + total
        media = f'{total/66:.1f}'
        disciplina_media_qntdade[disciplina] = media
    print('Quantidade Média de questões acertadas por Disciplina')
    for nota in disciplina_media_qntdade:
        print(f'{nota}:{disciplina_media_qntdade[nota]}')
    disciplina_media_qntdade_ordenado = dict(sorted(disciplina_media_qntdade.items(), key=lambda item: item[1]))
    disciplinas = list(disciplina_media_qntdade_ordenado.keys())
    medias = list(disciplina_media_qntdade_ordenado.values())
    plt.figure(figsize=(12, 6))
    cores = [disciplina_cor[disciplina] for disciplina in disciplinas]
    plt.bar(disciplinas, medias, color=cores,width=0.3)
    plt.xlabel('Disciplinas')
    plt.ylabel('Médias')
    plt.title('Quantidade Média de questões acertadas por Disciplina')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('quantidadeMediaPercentilREGULAR')
quantidadeMediaPercentilREGULAR()

