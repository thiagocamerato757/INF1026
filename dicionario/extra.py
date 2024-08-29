# Exemplo de dicionario: contando ocorrencias
'''
Escreva uma funcao que receba uma string e retorne um dicionario que represente
a tabela de frequencia dos caracteres na string, ou seja, um dicionario em que
cada elemento (item do dicionario) eh:
    caractere da string: quantidade de ocorrencias desse caractere na string

IDEIA DA SOLUCAO:
    cria um dicionario vazio
    para cada caractere na string
        se o caractere nao esta no dicionario:
            incluir no dicionario um novo elemento(item) caractere:1
        senao (caractere ja no dicionario):
            recuperar do dic a quantidade atual de ocorrencias do caractere
            atualizar a quantidade do caractere no dic, somando +1 ocorrencia

OBS1: se o caractere nao esta no dicionario, podemos considerar a quantidade
de ocorrencias atual como 0. Assim, usaremos dicionario.get(caractere,0).
Caso o caractere ja esteja no dicionario sera retornada a sua quantidade
ate o momento. Caso ele nao esteja no dicionario, sera retornado 0.

OBS2: Tanto a inclusao de um novo elemento quanto a atualizacao do valor de
um elemento ja existente sao feitas usando a atribuicao =>  dic[chave]=valor

'''

# Escreva aqui a função
def criaDicQtdOcorrencias(word:str) -> dict:
    dQtdOcorrencias :dict[str:int] = {}
    for ch in word:
        quantidade:int = dQtdOcorrencias.get(ch,0)+1
        dQtdOcorrencias[ch] = quantidade

    return dQtdOcorrencias
# BLOCO PRINCIPAL

sa= 'BANANAS MADURAS'
dQtdOcorrencias:dict[str:int] = criaDicQtdOcorrencias(sa)
print(sa)
print(dQtdOcorrencias)