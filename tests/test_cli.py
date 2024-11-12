from pytest import fixture, mark
from typer.testing import CliRunner

from pacote_python_tb.cli import app


@fixture
def cli_runner():
    return CliRunner()


def test_escala_cli_deve_retornar_0_ao_stdout(cli_runner):
    resultado = cli_runner.invoke(app, ['escala'])

    assert resultado.exit_code == 0


@mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_escala_cli_retornar_notas_resposta_nota_C(cli_runner, nota):
    resultado = cli_runner.invoke(app, ['escala'])

    assert nota in resultado.stdout


@mark.parametrize('nota', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'])
def test_escala_cli_retornar_notas_resposta_nota_D(cli_runner, nota):
    resultado = cli_runner.invoke(app, ['escala', 'D'])

    assert nota in resultado.stdout


@mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_escala_cli_retornar_todos_os_graus(cli_runner, grau):
    resultado = cli_runner.invoke(app, ['escala'])

    assert grau in resultado.stdout


def test_acorde_cli_deve_retornar_0_ao_stdout(cli_runner):
    resultado = cli_runner.invoke(app, ['acorde'])

    assert resultado.exit_code == 0


@mark.parametrize('nota', ['C', 'E', 'G'])
def test_acorde_cli_retornar_notas_resposta_nota_C(cli_runner, nota):
    resultado = cli_runner.invoke(app, ['acorde'])

    assert nota in resultado.stdout


@mark.parametrize('nota', ['D', 'F', 'A'])
def test_acorde_cli_retornar_notas_resposta_nota_D(cli_runner, nota):
    resultado = cli_runner.invoke(app, ['acorde', 'D'])

    assert nota in resultado.stdout


@mark.parametrize('graus', ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'])
def test_campo_harmonico_cli_retornar_todos_os_graus_C(cli_runner, graus):
    resultado = cli_runner.invoke(app, ['campo-harmonico', 'C', 'maior'])

    assert graus in resultado.stdout


@mark.parametrize('cifras', ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'])
def test_campo_harmonico_cli_retornar_todos_as_cifras_C(cli_runner, cifras):
    resultado = cli_runner.invoke(app, ['campo-harmonico', 'c', 'maior'])

    assert cifras in resultado.stdout


@mark.parametrize('graus', ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'])
def test_campo_harmonico_cli_retornar_todos_os_graus_D(cli_runner, graus):
    resultado = cli_runner.invoke(app, ['campo-harmonico', 'D', 'maior'])

    assert graus in resultado.stdout


@mark.parametrize('cifras', ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#°'])
def test_campo_harmonico_cli_retornar_todos_as_cifras_D(cli_runner, cifras):
    resultado = cli_runner.invoke(app, ['campo-harmonico', 'd', 'maior'])

    assert cifras in resultado.stdout


@mark.parametrize('graus', ['i', 'II°', 'III', 'iv', 'v', 'VI', 'VII'])
def test_campo_harmonico_cli_retornar_todos_os_graus_Cm(cli_runner, graus):
    resultado = cli_runner.invoke(app, ['campo-harmonico', 'c', 'menor'])

    assert graus in resultado.stdout


@mark.parametrize('cifras', ['Cm', 'D°', 'D#', 'Fm', 'Gm', 'G#', 'A#'])
def test_campo_harmonico_cli_retornar_todos_as_cifras_Cm(cli_runner, cifras):
    resultado = cli_runner.invoke(app, ['campo-harmonico', 'C', 'menor'])

    assert cifras in resultado.stdout
