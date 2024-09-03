# ========================================================
# Preenchimento obrigatorio do cabeçalho:
# NOME COMPLETO:  Thiago Pereira Camerato
# MATRICULA: 2212580
# TURMA: 33B
# PROF: Joisa
# ========================================================

# Questões do teste: 1A, 1B, 1C, 1D
# Alunos de TEMPO EXTRA: FAZER APENAS 1A, 1B, 1D

# Em uma universidade, após a conclusão do período, cada turma é representada
# por uma tupla com
# (codigoDaTurma, disciplina, professor, número de alunos, número de alunos
# aprovados)

# --------------------------------------------------------
# 1A) (vale 2.0)
# Escreva uma função, denominada avaliaPercAprovacao,  que:
# receba uma tupla correspondente a uma turma, calcule o percentual
# de aprovacao e determine a classificação da turma de acordo com
# o percentual de aprovação, e
# - retorne uma tupla com a avaliação contendo:
# (disciplina, professor, percentualDeAprovacao, classificação)

# Obviamente o percentual de aprovação é:
#     PercApv= número de aprovados/ número de alunos *100

# Classificação:
# •	PercApv < 30% – 'BaixaAprovacao'
# •	PercApv ≥30 até 50% – 'AprovacaoRegular'
# •	PercApv ≥50 até 80%– 'AltaAprovacao'.
# •	PercApv ≥80%– 'MuitoAltaAprovacao'.


# Escreva no espaço a seguir a função avaliaPercAprovacao:

def avaliaPercAprovacao(turma: tuple) -> tuple:
    percent: float = (turma[4] / turma[3]) * 100
    classificacao: str
    if (percent < 30):
        classificacao = 'BaixaAprovacao'
    elif (percent >= 30 and percent < 50):
        classificacao = 'AprovacaoRegular'
    elif (percent >= 50 and percent < 80):
        classificacao = 'AltaAprovacao'
    else:
        classificacao = 'MuitoAltaAprovacao'

    return turma[1], turma[2], percent, classificacao


# --------------------------------------------------------
# 1B) (vale 1.5)
# Escreva uma função, denominada avaliaTodasAsTurmas, que:
#    - receba uma tupla de turmas (tuplinhas com os dados das
#    turmas como descritas anteriormente) e
#    - retorne uma nova tupla com as
#    (tuplas das) avaliações de aprovação dessas turmas. Sua função deve
#    obrigatoriamente usar a função do item anterior.

# Escreva no espaço a seguir a função avaliaTodasAsTurmas:
def avaliaTodasAsTurmas(turmas: tuple) -> tuple:
    result: list[str] = []
    for turma in turmas:
        armazena: tuple = avaliaPercAprovacao(turma)
        result.append(armazena)

    return tuple(result)


# --------------------------------------------------------
# 1C) (vale 3.0)
# Escreva uma função, denominada criaDicDeProf, que:
#   - receba uma tupla de turmas (tuplinhas com os dados das
#   turmas como descritas anteriormente), e
#   - crie e retorne um dicionário com
#      CHAVE:  professor
#      VALOR: lista das turmas desse professor
# OBS: não pode criar o dicionário por enumeração

# Escreva no espaço a seguir a função
def criaDicDeProf(turmas: tuple) -> dict:
    result_dict: dict = {}
    for turma in turmas:
        lista_turmas: list = result_dict.get(turma[2], [])
        lista_turmas.append(turma)
        result_dict[turma[2]] = lista_turmas
    return result_dict


# --------------------------------------------------------
# 1D) (vale 3.5)
# Escreva uma função, denominada criaDicPorDiscClApv, que:
# - receba a tupla de (tuplas de) avaliações retornada pela função
# do item 1B, e
# - crie e retorne um dicionário com
#     CHAVE:  (disciplina, classificacaoDaAprovacao)
#     VALOR: quantidade de turmas dessa disciplina com essa classificação
# OBS: não pode criar o dicionário por enumeração

# Escreva no espaço a seguir a função criaDicPorDiscClApv
def criaDicPorDiscClApv(avaliacoes: tuple) -> dict:
    result_dict: dict = {}
    for avaliacao in avaliacoes:
        result_dict[(avaliacao[0], avaliacao[3])] = result_dict.get((avaliacao[0], avaliacao[3]), 0) + 1
    return result_dict


# --------------------------------------------------------
# BLOCO PRINCIPAL

# Teste sua função com a tupla de turmas abaixo:
tturmas = (('33A', 'FIS1111', 'VAVA', 56, 24), ('33B', 'MAT1212', 'NENA', 48, 43),
           ('33B', 'FIS1111', 'DEDE', 53, 51), ('33D', 'MAT1212', 'PEPE', 45, 20),
           ('33A', 'INF1010', 'NANA', 39, 21), ('33B', 'INF1010', 'DUDA', 28, 20),
           ('33D', 'INF1010', 'DUDA', 42, 12), ('33E', 'MAT1212', 'PEPE', 42, 39),
           ('33A', 'INF2020', 'DUDA', 30, 7), ('33B', 'INF2020', 'KAKA', 29, 13),
           ('33K', 'FIS1111', 'FAFA', 53, 12), ('33L', 'MAT1212', 'PEPE', 45, 35),
           ('33J', 'INF1010', 'NANA', 39, 24), ('33K', 'INF1010', 'DUDA', 28, 3),
           ('33M', 'INF2020', 'DUDA', 30, 13), ('33N', 'INF2020', 'KAKA', 26, 6),
           )

print('---Teste do item A : avaliação de 1 turma ---')
tu = ('33D', 'INF1010', 'DUDA', 42, 12)
av = avaliaPercAprovacao(tu)
print('Turma:', tu, '- Classificação:', av)

print('\n---Teste do item B : avaliações de todas as turmas ---')
taval = avaliaTodasAsTurmas(tturmas)
print(taval)

print('\n---Teste do item C : dic com listas de turmas por prof ---')
dProf = criaDicDeProf(tturmas)
print(dProf)

print('\n---Teste do item D : dic com qtd de turmas por (DISC,CLASSIFICAO APV) ---')
dDiscClas = criaDicPorDiscClApv(taval)
print(dDiscClas)

#########################################################################
# SAIDA ESPERADA PARA OS TESTES ACIMA:
# ---Teste do item A : avaliação de 1 turma ---
# Turma: ('33D', 'INF1010', 'DUDA', 42, 12) - Classificação: ('INF1010', 'DUDA', 28.57142857142857, 'BaixaAprovacao')

# ---Teste do item B : avaliações de todas as turmas ---
# (('FIS1111', 'VAVA', 42.857142857142854, 'AprovacaoRegular'),
#  ('MAT1212', 'NENA', 89.58333333333334, 'MuitoAltaAprovacao'),
#  ('FIS1111', 'DEDE', 96.22641509433963, 'MuitoAltaAprovacao'),
#  ('MAT1212', 'PEPE', 44.44444444444444, 'AprovacaoRegular'),
#  ('INF1010', 'NANA', 53.84615384615385, 'AltaAprovacao'),
#  ('INF1010', 'DUDA', 71.42857142857143, 'AltaAprovacao'),
#  ('INF1010', 'DUDA', 28.57142857142857, 'BaixaAprovacao'),
#  ('MAT1212', 'PEPE', 92.85714285714286, 'MuitoAltaAprovacao'),
#  ('INF2020', 'DUDA', 23.333333333333332, 'BaixaAprovacao'),
#  ('INF2020', 'KAKA', 44.827586206896555, 'AprovacaoRegular'),
#  ('FIS1111', 'FAFA', 22.641509433962266, 'BaixaAprovacao'),
#  ('MAT1212', 'PEPE', 77.77777777777779, 'AltaAprovacao'),
#  ('INF1010', 'NANA', 61.53846153846154, 'AltaAprovacao'),
#  ('INF1010', 'DUDA', 10.714285714285714, 'BaixaAprovacao'),
#  ('INF2020', 'DUDA', 43.333333333333336, 'AprovacaoRegular'),
#  ('INF2020', 'KAKA', 23.076923076923077, 'BaixaAprovacao'))

# ---Teste do item C : dic com listas de turmas por prof ---
# {'VAVA': [('33A', 'FIS1111', 'VAVA', 56, 24)], 'NENA': [('33B', 'MAT1212', 'NENA', 48, 43)],
#  'DEDE': [('33B', 'FIS1111', 'DEDE', 53, 51)],
#  'PEPE': [('33D', 'MAT1212', 'PEPE', 45, 20), ('33E', 'MAT1212', 'PEPE', 42, 39), ('33L', 'MAT1212', 'PEPE', 45, 35)],
#  'NANA': [('33A', 'INF1010', 'NANA', 39, 21), ('33J', 'INF1010', 'NANA', 39, 24)],
#  'DUDA': [('33B', 'INF1010', 'DUDA', 28, 20), ('33D', 'INF1010', 'DUDA', 42, 12),
#           ('33A', 'INF2020', 'DUDA', 30, 7), ('33K', 'INF1010', 'DUDA', 28, 3),
#           ('33M', 'INF2020', 'DUDA', 30, 13)],
#  'KAKA': [('33B', 'INF2020', 'KAKA', 29, 13), ('33N', 'INF2020', 'KAKA', 26, 6)],
#  'FAFA': [('33K', 'FIS1111', 'FAFA', 53, 12)]}

# ---Teste do item D : dic com qtd de turmas por (DISC,CLASSIFICAO APV) ---
# {('FIS1111', 'AprovacaoRegular'): 1, ('MAT1212', 'MuitoAltaAprovacao'): 2,
#  ('FIS1111', 'MuitoAltaAprovacao'): 1, ('MAT1212', 'AprovacaoRegular'): 1,
#  ('INF1010', 'AltaAprovacao'): 3, ('INF1010', 'BaixaAprovacao'): 2,
#  ('INF2020', 'BaixaAprovacao'): 2, ('INF2020', 'AprovacaoRegular'): 2,
#  ('FIS1111', 'BaixaAprovacao'): 1, ('MAT1212', 'AltaAprovacao'): 1}
