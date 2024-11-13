BRACO_GUITARRA = 'E F F# G G# A A# B C C# D D#'.split()

INTERVALOS = {
    'menor': [(0, 3), (0, 3), (0, 2), (0, 2), (0, 2), (0, 3)],
    'maior': [(0, 2), (0, 2), (-1, 1), (-1, 2), (-1, 2), (0, 2)],
}


def obter_posicao_nota(nota: str) -> int:
    """Retorna a posição de uma nota no braço da guitarra."""
    return BRACO_GUITARRA.index(nota)


def gerar_pentatonica(tonalidade: str, posicao_tonica: int) -> list[str]:
    """Gera a representação da escala pentatônica baseada na tonalidade e posição da tônica."""
    pentatonica = []

    for i, intervalo in enumerate(INTERVALOS[tonalidade]):
        parte_escala = '|--------' * (len(INTERVALOS[tonalidade]) - i - 1)
        parte_escala += f'|--{posicao_tonica + intervalo[0]}--{posicao_tonica + intervalo[1]}--|'
        parte_escala += '--------|' * i
        pentatonica.append(parte_escala)

    return pentatonica


def pentatonica(nota: str, tonalidade: str) -> str:
    """Retorna a escala pentatônica com base na nota e tonalidade."""
    nota = nota.upper()
    posicao_tonica = obter_posicao_nota(nota)
    pentatonica_lista = gerar_pentatonica(tonalidade, posicao_tonica)

    return '\n'.join(pentatonica_lista)
