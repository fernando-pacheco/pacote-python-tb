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
