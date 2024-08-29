def calcula_parcelas(valor_caixa: float, valor_presente: float) -> tuple:
    """
    Calculates the number of parcels and the total value based on the cash value and present value.

    Args:
        valor_caixa (float): The cash value.
        valor_presente (float): The present value.

    Returns:
        tuple: A tuple containing the number of parcels and the total value.
    """
    percent:float = valor_presente / valor_caixa
    if percent > 0.8:
        return 5, valor_presente + (0.10 * valor_presente)
    elif 0.5 < percent < 0.8:
        return 3, valor_presente + (0.08 * valor_presente)
    else:
        return 1, (0.95 * valor_presente)

if __name__ == "__main__":
    print(calcula_parcelas(1000, 1000))
    print(calcula_parcelas(1500, 1000))
    print(calcula_parcelas(2000, 1000))