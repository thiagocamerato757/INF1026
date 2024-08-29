# -*- coding: utf-8 -*-

# NOME: Thiago camerato
# TURMA: 33B
# MAT: INF1026
# PROF Joice

'''

Considere os seguintes dicionários com informações sobre as turmas de uma determinada
disciplina:
  dAlunoETurma : dicionário em que cada elemento  chave:valor  é ALUNO:TURMA
  dTurmaEProf : dicionário em que cada elemento  chave:valor  é TURMA:PROFESSOR

1) Escreva uma função, denominada constroiDicAlunoProf, que receba os dois dicionários como
 descritos acima e construa e retorne um novo dicionário com:
     CHAVE: aluno
     VALOR: professor do aluno


2) Escreva uma função denominada constroi dicTurmaQtdDeAlunos, que receba
    um dicionário com alunos e suas turmas, e construa e retorne um
    dicionário com:
        CHAVE: TURMA
        VALOR: Quantidade de alunos da turma

3) Escreva uma função denominada dictTurmaListaAlunos, que receba um dicionãrio com alunos
    e suas turmas e construa e retorne um dicionário com:
        CHAVE: TURMA
        VALOR: Lista de alunos da turma

'''


# Solucao do 1
def constroiDicAlunoProf(dict_aluno: dict[str:str], dict_prof: dict[str:str]) -> dict:
    result: dict[str:str] = {}
    for chave_aluno, valor_aluno in dict_aluno.items():
        result[chave_aluno] = dict_prof[valor_aluno]
    return result


# Solucao do 2
def dicTurmaQtdDeAlunos(dict_aluno: dict[str:str]) -> dict[str:int]:
    result: dict[str:int] = {}
    for chave_aluno, valor_aluno in dict_aluno.items():
        result[valor_aluno] = result.get(valor_aluno, 0) + 1
    return result

# solucao do 3
def dictTurmaListaAlunos(dict_aluno: dict[str:list[str]]) -> dict[str:list[str]]:
    result: dict[str:list[str]] = {}
    for chave_aluno, valor_aluno in dict_aluno.items():
        lista:list[str] = result.get(valor_aluno, [])
        lista.append(chave_aluno)
        result[valor_aluno] = lista
    return result

# BLOCO PRINCIPAL:
# Para testes :

dAlunoETurma = {'Nina': '33A', 'Dudu': '33E', 'Gigi': '33A', 'Vava': '33C', 'Kaka': '33C',
                'Zeze': '33B', 'Tata': '33D', 'Duda': '33A', 'Buba': '33C', 'Nena': '33E',
                'Vivi': '33A', 'Kadu': '33B', 'Tita': '33A', 'Lele': '33A', 'Lulu': '33C'}

dTurmaEProf = {'33A': 'LEO', '33B': 'VIK', '33C': 'MIA', '33D': 'EDU', '33E': 'AMY'}
if __name__ == '__main__':
    print("Ex1:\n")
    print(constroiDicAlunoProf(dAlunoETurma, dTurmaEProf))
    print()
    print("Ex2:\n")
    print(dicTurmaQtdDeAlunos(dAlunoETurma))
    print()
    print("Ex3:\n")
    print(dictTurmaListaAlunos(dAlunoETurma))
