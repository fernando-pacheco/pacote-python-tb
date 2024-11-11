from pytest import mark

from pacote_python_tb.acordes import acorde


def test_acordes_retorno_notas_correspondentes():
    nota = 'C'
    esperado = ['C', 'E', 'G']

    notas, _ = acorde(nota).values()

    assert esperado == notas


def test_acordes_retorno_graus_correspondentes():
    nota = 'C'
    esperado = ['I', 'III', 'V']

    _, graus = acorde(nota).values()

    assert esperado == graus


@mark.parametrize(
    'cifra,esperado',
    [
        ('C', ['C', 'E', 'G']),
        ('C#', ['C#', 'F', 'G#']),
        ('D', ['D', 'F#', 'A']),
        ('D#', ['D#', 'G', 'A#']),
        ('E', ['E', 'G#', 'B']),
        ('F', ['F', 'A', 'C']),
        ('F#', ['F#', 'A#', 'C#']),
        ('G', ['G', 'B', 'D']),
        ('G#', ['G#', 'C', 'D#']),
        ('A', ['A', 'C#', 'E']),
        ('A#', ['A#', 'D', 'F']),
        ('B', ['B', 'D#', 'F#']),
    ],
)
def test_acorde_maior_retorno_correto_notas(cifra, esperado):
    resultado = acorde(cifra)

    assert resultado['notas'] == esperado


@mark.parametrize(
    'cifra,esperado',
    [
        ('C°', ['C', 'D#', 'F#']),
        ('C#°', ['C#', 'E', 'G']),
        ('D°', ['D', 'F', 'G#']),
        ('D#°', ['D#', 'F#', 'A']),
        ('E°', ['E', 'G', 'A#']),
        ('F°', ['F', 'G#', 'B']),
        ('F#°', ['F#', 'A', 'C']),
        ('G°', ['G', 'A#', 'C#']),
        ('G#°', ['G#', 'B', 'D']),
        ('A°', ['A', 'C', 'D#']),
        ('A#°', ['A#', 'C#', 'E']),
        ('B°', ['B', 'D', 'F']),
    ],
)
def test_acorde_diminuto_retorno_correto_notas(cifra, esperado):
    resultado = acorde(cifra)

    assert resultado['notas'] == esperado


@mark.parametrize(
    'cifra,esperado',
    [
        ('Cm', ['C', 'D#', 'G']),
        ('C#m', ['C#', 'E', 'G#']),
        ('Dm', ['D', 'F', 'A']),
        ('D#m', ['D#', 'F#', 'A#']),
        ('Em', ['E', 'G', 'B']),
        ('Fm', ['F', 'G#', 'C']),
        ('F#m', ['F#', 'A', 'C#']),
        ('Gm', ['G', 'A#', 'D']),
        ('G#m', ['G#', 'B', 'D#']),
        ('Am', ['A', 'C', 'E']),
        ('A#m', ['A#', 'C#', 'F']),
        ('Bm', ['B', 'D', 'F#']),
    ],
)
def test_acorde_menor_retorno_correto_notas(cifra, esperado):
    resultado = acorde(cifra)

    assert resultado['notas'] == esperado


@mark.parametrize(
    'cifra,esperado',
    [
        ('C+', ['C', 'E', 'G#']),
        ('C#+', ['C#', 'F', 'A']),
        ('D+', ['D', 'F#', 'A#']),
        ('D#+', ['D#', 'G', 'B']),
        ('E+', ['E', 'G#', 'C']),
        ('F+', ['F', 'A', 'C#']),
        ('F#+', ['F#', 'A#', 'D']),
        ('G+', ['G', 'B', 'D#']),
        ('G#+', ['G#', 'C', 'E']),
        ('A+', ['A', 'C#', 'F']),
        ('A#+', ['A#', 'D', 'F#']),
        ('B+', ['B', 'D#', 'G']),
    ],
)
def test_acorde_maior_aumentado_retorno_correto_notas(cifra, esperado):
    resultado = acorde(cifra)

    assert resultado['notas'] == esperado


@mark.parametrize(
    'cifra,esperado',
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('C°', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
    ],
)
def test_acordes_retorno_correto_graus(cifra, esperado):
    resultado = acorde(cifra)

    assert resultado['graus'] == esperado
