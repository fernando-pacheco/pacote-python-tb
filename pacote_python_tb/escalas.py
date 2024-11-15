NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade

    Parameters:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala

    Returns:
        Um dicionário com as notas da escala e os graus

    Raises:
        ValueError: Caso a tônica não seja uma nota válida
        KeyError: Caso a escala não exista ou não seja implementada

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'menor')
        {'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    retorno = []

    tonica = tonica.upper()

    try:
        intervalos = ESCALAS[tonalidade]
        posicao_tonica = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f'Essa nota não existe, tente uma dessas: {NOTAS}')
    except KeyError:
        raise KeyError(
            f'Essa escala não existe ou não foi implementada. Tente uma dessas {list(ESCALAS.keys())}'
        )

    for intervalo in intervalos:
        nota = (posicao_tonica + intervalo) % len(NOTAS)
        retorno.append(NOTAS[nota])

    return {
        'notas': retorno,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
