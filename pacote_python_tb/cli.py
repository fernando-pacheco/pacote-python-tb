from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from pacote_python_tb.acordes import acorde as _acorde
from pacote_python_tb.campo_harmonico import (
    campo_harmonico as _campo_harmonico,
)
from pacote_python_tb.escalas import escala as _escala
from pacote_python_tb.pentatonica import pentatonica as _pentatonica

console = Console()
app = Typer()


@app.command()
def escala(
    tonica: str = Argument('c', help='Tônica da escala'),
    tonalidade: str = Argument('maior', help='Tonalidade da escala'),
):
    table = Table()
    notas, graus = _escala(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)

    console.print(table)


@app.command()
def acorde(
    cifra: str = Argument('C', help='Cifra de um acorde'),
):
    table = Table()
    notas, graus = _acorde(cifra).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)

    console.print(table)


@app.command()
def campo_harmonico(
    tonica: str = Argument('c', help='Tônica do campo harmônico'),
    tonalidade: str = Argument('maior', help='Tonalidade do campo harmônico'),
):
    table = Table()
    acordes, graus = _campo_harmonico(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*acordes)

    console.print(table)


@app.command()
def pentatonica(
    nota: str = Argument('A', help='Tônica do campo harmônico'),
    tonalidade: str = Argument('menor', help='Tonalidade do campo harmônico'),
):
    pentatonica = _pentatonica(nota, tonalidade)

    console.print(pentatonica)
