import pandas as pd

dados_brutos=pd.read_csv('./assets/Simulinho 2024 - Dados brutos - Sheet1.csv', dtype="str")

print(dados_brutos.iloc[1,1])
ranking_alunos = {}
def corrigir():
    linhas = dados_brutos.shape[0]
    colunas = dados_brutos.shape[1]
    #Para cada linha, vamos percorrer as colunas 
    for linha in range(1,linhas):
        aluno = dados_brutos.iloc[linha,1]
        aluno_status = {
        'total_acertos': 0,
        'matematica':0,
        "portugues":0,
        "quimica":0,
        "historia":0,
        "geografia":0,
        "fisica":0,
        "biologia":0,
        "filosofia-sociologia":0
    }
        for coluna in range(52,colunas): #A partir da coluna 52 temos os acertos em binario
            valor_binario = dados_brutos.iloc[linha,coluna]
            #verificando se o aluno acertou a questão
            if valor_binario=="1":
                aluno_status['total_acertos']+=1
                disciplina = dados_brutos.iloc[0,coluna]
                aluno_status[disciplina]+=1
                
        ranking_alunos[aluno] = aluno_status
    ranking_alunos_ordenado = dict(sorted(ranking_alunos.items(), key=lambda item: item[1]['total_acertos'], reverse=True))
    
    df = pd.DataFrame.from_dict(ranking_alunos_ordenado, orient='index')

    # Adicionar uma coluna com o CPF (supondo que os CPFs estão na primeira coluna dos dados brutos)
    df['cpf'] = list(ranking_alunos_ordenado.keys())[0::]

    # Reordenar as colunas
    df = df[['cpf', 'total_acertos', 'matematica', 'portugues', 'quimica', 'historia', 'geografia', 'fisica', 'biologia', 'filosofia-sociologia']]

    # Salvar o DataFrame em um arquivo CSV
    df.to_csv('ranking_alunos.xlsx', index=False)
corrigir()
for item in ranking_alunos :
        print(item,':',end='')
        print(ranking_alunos[item])

