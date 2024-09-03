def ordena(a:int, b:int, c:int) -> tuple:
    return tuple(sorted([a, b, c]))


def calcular_nota_final(notas_originalidade, notas_beleza):
    # Ordenando as notas de cada critério
    notas_originalidade = ordena(*notas_originalidade)
    notas_beleza = ordena(*notas_beleza)

    # Desprezando a maior e a menor nota de cada critério
    nota_media_originalidade = notas_originalidade[1]
    nota_media_beleza = notas_beleza[1]

    # Calculando a nota final
    nota_final = 0.6 * nota_media_originalidade + 0.4 * nota_media_beleza
    return nota_final


def processar_candidatos(arquivo):
    with open(arquivo, 'r') as f:
        for linha in f:
            dados = linha.strip().split(';')
            numero_inscricao = int(dados[0])
            notas_originalidade = list(map(float, dados[1:4]))
            notas_beleza = list(map(float, dados[4:7]))

            nota_final = calcular_nota_final(notas_originalidade, notas_beleza)

            print(f"Candidato {numero_inscricao}: Nota Final = {nota_final:.2f}")


# Exemplo de uso:
processar_candidatos('candidatos.txt')
