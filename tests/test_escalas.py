import pytest

import pacote_python_tb.escalas as pptb


def test_escalas_C_maior():
    esperado = {
        'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }

    resultado = pptb.escalas('C', 'maior')

    assert resultado == esperado


def test_escalas_A_maior():
    esperado = {
        'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }

    resultado = pptb.escalas('A', 'maior')

    assert resultado == esperado
