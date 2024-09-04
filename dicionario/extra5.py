############################################################
# QUESTAO 1
#
# A) Construa a função exibeDic que:
#     receba
#         - um dicionario qualquer e
#     exibe cada item do dicionário em uma linha  no seguinte formato:
#       "xxxxxx  --> yyyyyyy.yy"
#       xxxxx é a chave e yyyyy, um valor numérico
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Escreva abaixo a solução da questão 1):
def exibeDic(dicio:dict)->None:
    for chave, valor in dicio.items():
        print(f'{chave} --> {valor:.2f}')

############################################################
############################################################
# QUESTAO 2
# Deseja-se analisar o impacto fiscal das vendas realizadas por uma loja que
# comercializa diversos tipos de produtos.
# Para isso, você deve desenvolver uma série de funções em Python que permitam
# calcular os impostos aplicáveis sobre cada venda e apresentar um resumo
# detalhado por tipo de produto.
#
# Considere as seguintes estruturas:

# ==> 1.	Tupla ttipos_produtos_impostos: Uma tupla onde cada item é uma tuplinha
#       contendo:
#       •	Tipo de Produto: A categoria do produto (ex.: "Móveis", "Eletrodomésticos").
#       •	Tipo de Imposto: O tipo de imposto aplicável (ex.: "ICMS", "IPI").
#       •	Percentual: O percentual do imposto aplicável.

#   Exemplo de uma tupla tipos_produtos_impostos:

#           ttipos_produtos_impostos = (
#                   ("Móveis", "ICMS", 12), ("Móveis", "IPI", 5),
#                   ("Móveis", "PIS", 1.65),("Eletrodomésticos", "ICMS", 18))


# ==>2) dicionário dproduto_tipo: Us para seus tipos de produto.:
#       •	a chave é o nome do produto e
#       •	o valor é  o tipo de produto

#   Exemplo de um dicionário dprodutos_por_tipo:

#           dproduto_tipo = {
#               "Cadeira": "Móveis",
#               "Mesa": "Móveis",
#               "Geladeira": "Eletrodomésticos"}


# ==> 3) dicionário dtipo_produto_impostos onde:
#       •	a chave é o tipo do produto e
#       •	o valor é uma tupla contendo os nomes dos impostos aplicáveis

#    Exemplo de um dicionário dimpostos_tipos_produto:

#         dtipo_produto_impostos = {
#             "Móveis": ("ICMS", "IPI", "PIS"),
#             "Eletrodomésticos": ("ICMS", )}


# ==> 4.	Tupla tcompras_clientes: Uma tupla contendo registros de compras realizadas
#        por clientes. Cada item na tupla é uma tuplinha com:
#        •	Nome do Cliente: O nome do cliente que realizou a compra.
#       •	Produto Comprado: O produto adquirido pelo cliente.
#       •	Data da Compra: A data em que a compra foi realizada.
#       •	Valor da Compra: O valor total pago pelo cliente.

#   Exemplo de uma tupla tipos_produtos_impostos:

#           tcompras_clientes = (
#                       ("Lara", "Cadeira", "01/08/2024", 150.0),
#                       ("João", "Mesa", "12/08/2024", 300.0))


# ..............................................................................
############################################################
# A) Construa a função criaDicPercentuaisImpostos que:
#     receba
#         - tupla tipos_produtos_impostos, tupla de tuplinhas com (tipo produto, tipo imposto, percentual)
#     e retorne um dicionário onde
#           a chave é uma tupla (tipo_produto, tipo_imposto)
#           o valor é o percentual do imposto.
# OBS: não há  (tipo_produto, tipo_imposto) repetido na tupla de entrada
# --------------------------------------------------------------------
# Escreva abaixo a solução da questão 2A):
def criaDicPercentuaisImpostos(tipos_produtos_impostos:tuple)->dict:
    dicionario:dict = {}
    for tipo_produto,tipo_imposto, percentual in tipos_produtos_impostos:
        dicionario[(tipo_produto, tipo_imposto)] = percentual
    return dicionario

# --------------------------------------------------------------------

############################################################
# B) Construa a função calcValorTotImpostosExibeValorAPagar que:
#     receba
#        - tupla de compras dos clientes, tupla de tuplinhas com (nome,produto,data,valor)
#        - o dicionário de percentuais de impostos (criado no item a)
#        - o dicionário que mapeia produto a tipo do produto (dproduto_tipo)
#        - o dicionário que mapeia o tipo de  produto aos impostos (dtipo_produto_impostos)
#  . A função deve:
#    -->  calcular o valor total de impostos para cada compra,exibindo
#    o nome do cliente, o produto, o valor da compra, o valor total dos impostos e
#    o valor final
#    --> 	Retornar uma tupla onde cada item contém:
#        o tipo de produto, e o valor total de imposto pago.
#
# --------------------------------------------------------------------
# Escreva abaixo a solução da questão 2B):
def calcValorTotImpostosExibeValorAPagar(tcompras_clientes:tuple, dic_percentuais_impostos:dict, dprodutos_por_tipo:dict, dtipo_produto_impostos:dict)->tuple:


# --------------------------------------------------------------------

############################################################
# C) Construa a função calTotalImpostoPorTipoProduto que:
#     receba
#         - a tupla resultante da função 2  e
#     e retorne um novo dicionário onde:
#         chave: tipo de produto
#         valor: valor total de imposto pago
# OBS: apenas os tipos de impostos que aparecem na tupla de entrada devem ser
#     incluídos no dicionário resultante
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Escreva abaixo a solução da questão 2C):


##########################################################################
# QUESTAO 3:
# Considere o dicionário de ingressos para shows (dIngPorShow)
#  Um dicionário de dicionários que armazena as informações dos ingressos para
#  cada show.
#  O dicionário tem  como:
#      chave:  nome do show, e
#      valor: um dicionário onde:
#          Chave: O tipo de ingresso (ex.: "VIP", "Pista", "Camarote", "Arquibancada", "Gramado").
#          Valor: O valor do ingresso.
#
# A) Construa a função exibeValorIngresso que:
#     receba
#         - o nome do show
#         - o tipo de ingresso
#         - o dicionário dIngPorShow
#     e exibe na tela uma das seguintes mensagens:
#        Nome do show - 'show inexistente', se o nome do show recebido não está no dicionário
#        Nome do show - tipo de ingresso - 'tipo de ingresso inexistente para este show', se a show não disponibiliza o tipo de ingresso recebido
#        Nome do show - tipo de ingresso - valor do ingresso, caso contrário

# No bloco principal, na área de teste da questão 2, você deve fazer 3
# testes contemplando cada uma das 3 possibilidades (show inexistente, tipo
# não disponibilizado  e tudo ok)

# --------------------------------------------------------------------
# Escreva abaixo a solução da questão 3A):


############################################################
############################################################
# Bloco Principal

# tuplas para os testes da questão 2
ttipos_produtos_impostos = (
    ("Móveis", "ICMS", 12),
    ("Móveis", "IPI", 5),
    ("Móveis", "PIS", 1.65),
    ("Eletrodomésticos", "ICMS", 18),
    ("Eletrodomésticos", "IPI", 10),
    ("Eletrodomésticos", "COFINS", 7.6),
    ("Eletrônicos", "ICMS", 18),
    ("Eletrônicos", "IPI", 10),
    ("Eletrônicos", "PIS", 1.65),
    ("Vestuário", "ICMS", 12),
    ("Vestuário", "IPI", 5),
    ("Vestuário", "COFINS", 7.6),
    ("Alimentos", "ICMS", 7),
    ("Alimentos", "IPI", 4),
    ("Alimentos", "PIS", 1.65),
    ("Bebidas", "ICMS", 20),
    ("Bebidas", "IPI", 15),
    ("Bebidas", "COFINS", 9),
    ("Cosméticos", "ICMS", 18),
    ("Cosméticos", "IPI", 10),
    ("Cosméticos", "PIS", 1.65),
    ("Medicamentos", "ICMS", 12),
    ("Medicamentos", "IPI", 5),
    ("Medicamentos", "PIS", 1.65),
)

tcompras_clientes = (
    ("Lara", "Cadeira", "2024-08-01", 150.0),
    ("João", "Mesa", "2024-08-02", 300.0),
    ("Ana", "Geladeira", "2024-08-03", 2500.0),
    ("José", "Fogão", "2024-08-04", 1200.0),
    ("Paula", "Notebook", "2024-08-05", 5000.0),
    ("Beto", "Smartphone", "2024-08-06", 3500.0),
    ("Rita", "Camiseta", "2024-08-07", 50.0),
    ("Vera", "Calça", "2024-08-08", 120.0),
    ("Léo", "Perfume", "2024-08-09", 200.0),
    ("Toni", "Televisão", "2024-08-10", 3200.0),
    ("Dani", "Arroz", "2024-08-11", 25.0),
    ("Cris", "Feijão", "2024-08-12", 10.0),
    ("Mara", "Leite", "2024-08-13", 4.5),
    ("Nina", "Cerveja", "2024-08-14", 30.0),
    ("Rafa", "Vinho", "2024-08-15", 80.0),
    ("Bia", "Shampoo", "2024-08-16", 15.0),
    ("Lina", "Paracetamol", "2024-08-17", 8.0),
    ("Zeca", "Sofá", "2024-08-18", 1800.0),
    ("João", "Microondas", "2024-08-19", 450.0),
    ("Toni", "Televisão", "2024-08-20", 2800.0),
    ("Beto", "Camiseta", "2024-08-21", 45.0),
    ("Lara", "Mesa", "2024-08-22", 350.0),
    ("Bia", "Cadeira", "2024-08-23", 160.0),
    ("Léo", "Perfume", "2024-08-24", 220.0),
    ("Mara", "Notebook", "2024-08-25", 4800.0),
)

# Dicionários para testes da questão 2

dproduto_tipo = {
    "Cadeira": "Móveis",
    "Mesa": "Móveis",
    "Sofá": "Móveis",
    "Geladeira": "Eletrodomésticos",
    "Fogão": "Eletrodomésticos",
    "Microondas": "Eletrodomésticos",
    "Televisão": "Eletrônicos",
    "Notebook": "Eletrônicos",
    "Smartphone": "Eletrônicos",
    "Camiseta": "Vestuário",
    "Calça": "Vestuário",
    "Casaco": "Vestuário",
    "Arroz": "Alimentos",
    "Feijão": "Alimentos",
    "Leite": "Alimentos",
    "Cerveja": "Bebidas",
    "Vinho": "Bebidas",
    "Perfume": "Cosméticos",
    "Shampoo": "Cosméticos",
    "Paracetamol": "Medicamentos",
}

dtipo_produto_impostos = {
    "Móveis": ("ICMS", "IPI", "PIS"),
    "Eletrodomésticos": ("ICMS", "IPI", "COFINS"),
    "Eletrônicos": ("ICMS", "IPI", "PIS"),
    "Vestuário": ("ICMS", "IPI", "COFINS"),
    "Alimentos": ("ICMS", "IPI", "PIS"),
    "Bebidas": ("ICMS", "IPI", "COFINS"),
    "Cosméticos": ("ICMS", "IPI", "PIS"),
    "Medicamentos": ("ICMS", "IPI", "PIS"),
}

# questão 3
dIngPorShow = {
    "Show do Rock": {
        "Pista": 200.0, "Camarote": 800.0, "Arquibancada": 150.0, "Gramado": 100.0},
    "Show do Jazz": {
        "VIP": 600.0, "Pista": 250.0, "Camarote": 900.0, },
    "Show do Pop": {
        "VIP": 600.0, "Pista": 300.0, "Arquibancada": 200.0, "Gramado": 150.0},
}

############################################################
# Retire os # nas linhas de teste da questão 1
print('\n-----Teste da questão 1-----')
# exibeDic({'chv1':2,'chv2':19.98877})


############################################################
# Retire os # nas linhas de teste da questão 2A
print('\n-----Teste da questão 2A-----')
# dic_percentuais_impostos=criaDicPercentuaisImpostos(ttipos_produtos_impostos)
# exibeDic(dic_percentuais_impostos)
# # print(dic_percentuais_impostos) # caso vc não tenha feito a questão 1

############################################################
# Retire os # nas linhas de teste da questão 2B
# ''' utilize o dicionário abaixo, caso vc não tenha feito o item 1A'''
# #dic_percentuais_impostos={('Móveis', 'ICMS'): 12, ('Móveis', 'IPI'): 5, ('Móveis', 'PIS'): 1.65, ('Eletrodomésticos', 'ICMS'): 18, ('Eletrodomésticos', 'IPI'): 10, ('Eletrodomésticos', 'COFINS'): 7.6, ('Eletrônicos', 'ICMS'): 18, ('Eletrônicos', 'IPI'): 10, ('Eletrônicos', 'PIS'): 1.65, ('Vestuário', 'ICMS'): 12, ('Vestuário', 'IPI'): 5, ('Vestuário', 'COFINS'): 7.6, ('Alimentos', 'ICMS'): 7, ('Alimentos', 'IPI'): 4, ('Alimentos', 'PIS'): 1.65, ('Bebidas', 'ICMS'): 20, ('Bebidas', 'IPI'): 15, ('Bebidas', 'COFINS'): 9, ('Cosméticos', 'ICMS'): 18, ('Cosméticos', 'IPI'): 10, ('Cosméticos', 'PIS'): 1.65, ('Medicamentos', 'ICMS'): 12, ('Medicamentos', 'IPI'): 5, ('Medicamentos', 'PIS'): 1.65}
# print('\n-----Teste da questão 2B-----')
# tupla_resultante=calcValorTotImpostosExibeValorAPagar(tcompras_clientes, dic_percentuais_impostos, dproduto_tipo, dtipo_produto_impostos)


############################################################
# Retire os # nas linhas de teste da questão 2C
# ''' utilize a tupla abaixo, caso vc não tenha feito o item 1B'''
# #tupla_resultante=(('Móveis', 27.975), ('Móveis', 55.95), ('Eletrodomésticos', 890.0), ('Eletrodomésticos', 427.2), ('Eletrônicos', 1482.5), ('Eletrônicos', 1037.75), ('Vestuário', 12.3), ('Vestuário', 29.519999999999996), ('Cosméticos', 59.3), ('Eletrônicos', 948.8), ('Alimentos', 3.1625), ('Alimentos', 1.2650000000000001), ('Alimentos', 0.56925), ('Bebidas', 13.2), ('Bebidas', 35.2), ('Cosméticos', 4.447499999999999), ('Medicamentos', 1.492), ('Móveis', 335.7), ('Eletrodomésticos', 160.2), ('Eletrônicos', 830.2), ('Vestuário', 11.07), ('Móveis', 65.275), ('Móveis', 29.84), ('Cosméticos', 65.23), ('Eletrônicos', 1423.2))

# print('\n-----Teste da questão 2c-----')
# dTipoImpostos=calTotalImpostoPorTipoProduto(tupla_resultante)
# exibeDic(dTipoImpostos)
# # print(dTipoImpostos) # caso vc não tenha feito a questão 1


############################################################
# Escreva os 3 testes pedidos na questão 3
print('\n-----Testes da questão 3-----')


