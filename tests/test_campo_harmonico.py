from pytest import mark

from pacote_python_tb.campo_harmonico import campo_harmonico


@mark.parametrize(
    'tonica,esperado',
    [
        ('C', ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°']),
        ('C#', ['C#', 'D#m', 'Fm', 'F#', 'G#', 'A#m', 'C°']),
        ('D', ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#°']),
        ('D#', ['D#', 'Fm', 'Gm', 'G#', 'A#', 'Cm', 'D°']),
        ('E', ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#°']),
        ('F', ['F', 'Gm', 'Am', 'A#', 'C', 'Dm', 'E°']),
        ('F#', ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'F°']),
        ('G', ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#°']),
        ('G#', ['G#', 'A#m', 'Cm', 'C#', 'D#', 'Fm', 'G°']),
        ('A', ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#°']),
        ('A#', ['A#', 'Cm', 'Dm', 'D#', 'F', 'Gm', 'A°']),
        ('B', ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#°']),
    ],
)
def test_campo_harmonico_maior_retorno_das_cifras(tonica, esperado):
    resultado = campo_harmonico(tonica, 'maior')

    assert resultado['acordes'] == esperado


@mark.parametrize(
    'tonica,esperado',
    [
        ('A', ['Am', 'B°', 'C', 'Dm', 'Em', 'F', 'G']),
        ('A#', ['A#m', 'C°', 'C#', 'D#m', 'Fm', 'F#', 'G#']),
        ('B', ['Bm', 'C#°', 'D', 'Em', 'F#m', 'G', 'A']),
        ('C', ['Cm', 'D°', 'D#', 'Fm', 'Gm', 'G#', 'A#']),
        ('C#', ['C#m', 'D#°', 'E', 'F#m', 'G#m', 'A', 'B']),
        ('D', ['Dm', 'E°', 'F', 'Gm', 'Am', 'A#', 'C']),
        ('D#', ['D#m', 'F°', 'F#', 'G#m', 'A#m', 'B', 'C#']),
        ('E', ['Em', 'F#°', 'G', 'Am', 'Bm', 'C', 'D']),
        ('F', ['Fm', 'G°', 'G#', 'A#m', 'Cm', 'C#', 'D#']),
        ('F#', ['F#m', 'G#°', 'A', 'Bm', 'C#m', 'D', 'E']),
        ('G', ['Gm', 'A°', 'A#', 'Cm', 'Dm', 'D#', 'F']),
        ('G#', ['G#m', 'A#°', 'B', 'C#m', 'D#m', 'E', 'F#']),
    ],
)
def test_campo_harmonico_menor_retorno_das_cifras(tonica, esperado):
    resultado = campo_harmonico(tonica, 'menor')

    assert resultado['acordes'] == esperado


@mark.parametrize(
    'tonica,esperado',
    [('E', ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'])],
)
def test_campo_harmonico_maior_retorno_dos_graus(tonica, esperado):
    resultado = campo_harmonico(tonica, 'maior')

    assert resultado['graus'] == esperado


@mark.parametrize(
    'tonica,esperado',
    [('E', ['i', 'II°', 'III', 'iv', 'v', 'VI', 'VII'])],
)
def test_campo_harmonico_menor_retorno_dos_graus(tonica, esperado):
    resultado = campo_harmonico(tonica, 'menor')

    assert resultado['graus'] == esperado
