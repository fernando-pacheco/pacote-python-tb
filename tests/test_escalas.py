from pytest import fixture, mark, raises

from pacote_python_tb.escalas import *


@fixture
def mock_retorno_esperado_C_maior():
    return {
        'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }


def test_escalas_C_maior(mock_retorno_esperado_C_maior):
    esperado = mock_retorno_esperado_C_maior
    resultado = escala('C', 'maior')

    assert resultado == esperado


def test_escala_retorno_7_graus(mock_retorno_esperado_C_maior):
    tonica = 'c'
    tonalidade = 'maior'

    esperado = mock_retorno_esperado_C_maior['graus']
    resultado = escala(tonica, tonalidade)['graus']

    assert resultado == esperado


def test_escala_entrada_notas_minusculas(mock_retorno_esperado_C_maior):
    tonica = 'c'
    tonalidade = 'maior'

    esperado = mock_retorno_esperado_C_maior
    resultado = escala(tonica, tonalidade)

    assert resultado == esperado


def test_escala_entrada_de_nota_nao_existente():
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_erro = f'Essa nota não existe, tente uma dessas: {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert mensagem_erro == error.value.args[0]


def test_escala_entrada_de_escala_nao_existente():
    tonica = 'c'
    tonalidade = 'tonalidade'

    mensagem_erro = f'Essa escala não existe ou não foi implementada. Tente uma dessas {list(ESCALAS.keys())}'

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_erro == error.value.args[0]


@mark.parametrize(
    'tonica,esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('D', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('D#', ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D']),
        ('E', ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('F#', ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']),
        ('G', ['G', 'A', 'B', 'C', 'D', 'E', 'F#']),
        ('G#', ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']),
        ('A', ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']),
        ('A#', ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']),
        ('B', ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']),
    ],
)
def test_escala_maior_retorno_correto_notas(tonica, esperado):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado


@mark.parametrize(
    'tonica,esperado',
    [
        ('C', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('D', ['D', 'E', 'F', 'G', 'A', 'A#', 'C']),
        ('D#', ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#']),
        ('E', ['E', 'F#', 'G', 'A', 'B', 'C', 'D']),
        ('F', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
        ('F#', ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E']),
        ('G', ['G', 'A', 'A#', 'C', 'D', 'D#', 'F']),
        ('G#', ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#']),
        ('A', ['A', 'B', 'C', 'D', 'E', 'F', 'G']),
        ('A#', ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#']),
        ('B', ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']),
    ],
)
def test_escala_menor_retorno_correto_notas(tonica, esperado):
    resultado = escala(tonica, 'menor')
    assert resultado['notas'] == esperado
