def converter_segundos(tempo_em_segundos : int) -> tuple:
    horas:int = tempo_em_segundos // 3600
    minutos:int= (tempo_em_segundos % 3600) // 60
    segundos:int = tempo_em_segundos % 60
    return horas, minutos, segundos


def processar_maratona(arquivo_atletas: str) -> None:
    atleta_mais_rapido: tuple = None
    atleta_mais_lento: tuple = None
    menor_tempo: float = float('inf') # Inicializa com infinito positivo
    maior_tempo: float = 0

    with open(arquivo_atletas, 'r') as file:
        for linha in file:
            dados = linha.strip().split()  # Usa split() sem argumentos para separar por qualquer quantidade de espaços

            # Verifica se a linha tem dois valores (inscrição e tempo)
            if len(dados) != 2:
                print(f"Linha inválida ou mal formatada: '{linha.strip()}'")
                continue

            inscricao, tempo_em_segundos = dados
            inscricao = int(inscricao)
            tempo_em_segundos = int(tempo_em_segundos)

            # Verifica desclassificação
            if tempo_em_segundos > 36000:
                print(f"Atleta {inscricao} desclassificado por tempo superior a 10 horas.")
                continue

            horas, minutos, segundos = converter_segundos(tempo_em_segundos)
            print(f"Atleta {inscricao}: {horas:02}:{minutos:02}:{segundos:02}")

            # Verifica se é o mais rápido
            if tempo_em_segundos < menor_tempo:
                menor_tempo = tempo_em_segundos
                atleta_mais_rapido = (inscricao, menor_tempo)

            # Verifica se é o mais lento
            if tempo_em_segundos > maior_tempo:
                maior_tempo = tempo_em_segundos
                atleta_mais_lento = (inscricao, maior_tempo)

    if atleta_mais_rapido:
        horas, minutos, segundos = converter_segundos(atleta_mais_rapido[1])
        print(f"\nAtleta mais rápido: {atleta_mais_rapido[0]} com tempo {horas:02}:{minutos:02}:{segundos:02}")

    if atleta_mais_lento:
        horas, minutos, segundos = converter_segundos(atleta_mais_lento[1])
        print(f"Atleta mais lento: {atleta_mais_lento[0]} com tempo {horas:02}:{minutos:02}:{segundos:02}")

if __name__ == "__main__":
    processar_maratona("atletas.txt")