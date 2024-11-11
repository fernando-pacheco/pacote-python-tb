from pytest import fixture, mark
from typer.testing import CliRunner

from pacote_python_tb.cli import app


@fixture
def cli_runner():
    return CliRunner()


def test_escala_cli_deve_retornar_0_ao_stdout(cli_runner):
    resultado = cli_runner.invoke(app)

    assert resultado.exit_code == 0


@mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_escala_retornar_notas_resposta_nota_C(cli_runner, nota):
    resultado = cli_runner.invoke(app)

    assert nota in resultado.stdout


@mark.parametrize('nota', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'])
def test_escala_retornar_notas_resposta_nota_D(cli_runner, nota):
    resultado = cli_runner.invoke(app, ['D'])

    assert nota in resultado.stdout


@mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_escala_retornar_todos_os_graus(cli_runner, grau):
    resultado = cli_runner.invoke(app)

    assert grau in resultado.stdout
