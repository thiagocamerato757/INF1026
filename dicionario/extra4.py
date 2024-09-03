# Considere um dicionário com os preços de um certo grupo de produtos nos supermercados,
# em que cada item é:
# MERCADO: dicionário internos com produtos e respectivos preços nesse mercado
# Exemplo:
# {'Qbarato': {'biscoito': 4.3, 'leite': 3.2, 'suco': 7.1, 'chocolate': 6.4, 'detergente': 3.2,
# 'cerveja': 6.4, 'manteiga': 8.7},
# 'UltraK': {'biscoito': 3.5, 'leite': 3.3, 'suco': 8.9, 'chocolate': 6.9, 'detergente': 4.2,
# 'cerveja': 6.4, 'manteiga': 8.7},
# 'Market': {'biscoito': 4.5, 'leite': 3.2, 'suco': 7.5, 'chocolate': 6.6, 'detergente': 3.8,
# 'cerveja': 6.5, 'manteiga': 9.2},
# 'Preferido': {'biscoito': 4.65, 'leite': 3.4, 'suco': 8.1, 'chocolate': 8.1, 'detergente': 3.3,
# 'cerveja': 6.5, 'manteiga': 8.9},
# 'Escolhido': {'biscoito': 5.2, 'leite': 3.3, 'suco': 8.3, 'chocolate': 7.5, 'detergente': 3.9,
# 'cerveja': 6.4, 'manteiga': 8.6}}
# Para os itens 1 , 2 e 3 deve ser considerado o dicionário acima
#
# 1) Escreva a função totalDaCompra que:
# - recebe o dicionário de mercados descrito, um segundo dicionário que representa a lista de
# compras de uma pessoa e o nome de um Mercado
# Esse segundo dicionário (a lista de compras) tem as seguintes informações:
# dCompras = { PRODUTO1: QUANT1, PRODUTO2:QUANT2, PRODUTO3:QUANT3 ...}
# Retorna o valor total das compras nesse mercado
# OBS: Pode assumir que todos os produtos do dic de compras estão nos dicionários de produtos
# com preços de todos os mercados
# (Mas faça uma segunda versão considerando que produtos do dic de compras podem não
# constar em alguns dos mercados)
def totalDaCompra(mercados:dict, compras:dict, nomeMercado:str)->int:
    total:int = 0
    for produto,qtd in compras.items():
        total+= mercados[nomeMercado].get(produto,0) * qtd
    return total
#
# 2) Escreva a função criaDTotalDaCompra que:
# - recebe o dicionário de mercados descrito e um segundo dicionário que representa a lista de
# compras de uma pessoa. Esse dicionário (a lista de compras) tem as seguintes informações:
# dCompras = { PRODUTO1: QUANT1, PRODUTO2:QUANT2, PRODUTO3:QUANT3 ...}
# Obs: quantidades são sempre um número inteiro
# - retorna um novo dicionário onde cada item é :
# MERCADO : valorTotalDaCompra nesse mercado
def criaDTotalDaCompra(mercados:dict, compras:dict)->dict:
    dTotal:dict = {}
    for nomeMercado,produtos in mercados.items():
        dTotal[nomeMercado] = totalDaCompra(mercados,compras,nomeMercado)
    return dTotal

# 3) Escreva a função criaDicMercadosPorProd que:
# - recebe o dicionário de mercados
# - constrói e retorna o dicionário de produtos. O dicionário de produtos é um dicionário de
# dicionários onde cada item é:
# PRODUTO: {dicionário com mercados e preço nos mercados desse produto }
# EXEMPLO:
# Se a função recebesse o dicionário abaixo
# dPorMerc = { ‘QBARATO’: {‘BISCOITO ‘ : 4.15, ‘MANTEIGA’ : 8.70} ,
# ‘ULTRAK’: {‘BISCOITO ‘ : 5.20, ‘MANTEIGA’ : 8.80
# }
#
# Seria retornado o seguinte dicionário:
# dPorProd = { ‘BISCOITO’: {‘QBARATO : 4.15, ‘ULTRAK’ : 5.20},
# ‘MANTEIGA’: {‘QBARATO’ : 8.70, ‘ULTRAK’ : 8.80},
# }
def criaDicMercadosPorProd(mercados:dict)->dict:
    dPorProd:dict = {}
    for nomeMercado,produtos in mercados.items():
        for nomeProd,preco in produtos.items():
            dPorProd[nomeProd] = dPorProd.get(nomeProd, {})
            dPorProd[nomeProd][nomeMercado] = preco
    return dPorProd

# CONSTRUA O PROGRAMA COMPLETO COM AS FUNÇÕES< UM BLOCO PRINCIPAL COM O
# DICIONARIO DO EXEMPLO, SEGUIDO DAS CHAMADAS DAS FUNÇÕES E EXIBIÇÃO APROPRIADA
# DOS RESULTADOS
if __name__ == "__main__":
    mercados = {
        'Qbarato': {'biscoito': 4.3, 'leite': 3.2, 'suco': 7.1, 'chocolate': 6.4, 'detergente': 3.2,
                    'cerveja': 6.4, 'manteiga': 8.7},
        'UltraK': {'biscoito': 3.5, 'leite': 3.3, 'suco': 8.9, 'chocolate': 6.9, 'detergente': 4.2,
                   'cerveja': 6.4, 'manteiga': 8.7},
        'Market': {'biscoito': 4.5, 'leite': 3.2, 'suco': 7.5, 'chocolate': 6.6, 'detergente': 3.8,
                   'cerveja': 6.5, 'manteiga': 9.2},
        'Preferido': {'biscoito': 4.65, 'leite': 3.4, 'suco': 8.1, 'chocolate': 8.1, 'detergente': 3.3,
                      'cerveja': 6.5, 'manteiga': 8.9},
        'Escolhido': {'biscoito': 5.2, 'leite': 3.3, 'suco': 8.3, 'chocolate': 7.5, 'detergente': 3.9,
                      'cerveja': 6.4, 'manteiga': 8.6}
    }

    dCompras = {'biscoito': 2, 'leite': 3, 'chocolate': 1}

    # Chamada da função totalDaCompra
    total_qbarato = totalDaCompra(mercados, dCompras, 'Qbarato')
    print(f"Total da compra no Qbarato: R${total_qbarato:.2f}")
    print()
    # Chamada da função criaDTotalDaCompra
    dTotalCompra = criaDTotalDaCompra(mercados, dCompras)
    print("Total da compra em cada mercado:")
    for mercado, total in dTotalCompra.items():
        print(f"{mercado}: R${total:.2f}")
    print()
    # Chamada da função criaDicMercadosPorProd
    dPorProd = criaDicMercadosPorProd(mercados)
    print("Dicionário de mercados por produto:")
    for produto, precos in dPorProd.items():
        print(f"{produto}: {precos}")
