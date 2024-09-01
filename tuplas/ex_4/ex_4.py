def ehPerfeito(numero: int) -> tuple[bool, list[int]]:
    divisores: list[int] = [i for i in range(1, numero) if numero % i == 0]
    soma_divisores: int = sum(divisores)
    return soma_divisores == numero, divisores

def avaliaNumero(numero: int)-> None:
    eh_perfeito, divisores = ehPerfeito(numero)
    print(f"Número: {numero}")
    print(f"Divisores (excluindo ele mesmo): {divisores}")
    if eh_perfeito:
        print(f"{numero} é um número perfeito!")
    else:
        print(f"{numero} não é um número perfeito.")

if __name__ == "__main__":
    avaliaNumero(6)
    avaliaNumero(28)
    avaliaNumero(100)
    avaliaNumero(496)
    avaliaNumero(8128)