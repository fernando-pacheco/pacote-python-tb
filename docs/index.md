<!-- ![logo do projeto](assets/logo.png){width="300" .classe-css} -->
# Pacote Python TB

## Como usar?

Você pode chamar as escalas via linha de comando. Por exemplo:
```bash
poetry run escalas
```
Retornando os graus e as notas correspondentes a essa escala:
```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

## Alteração da tônica da escala

O primeiro parametro do CLI é a tônica da escala que sedeja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala de `F#`:
```bash
poetry run escalas F#
```
Retornando:
```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

## Alteração a tonalidade da escala

Você pode alterar a tonalidade da escala também! Esse é o segundo parâmetro da linha de comando. Por exemplo, a escala de `D#` maior:
```bash
poetry run escalas B maior
```
Retornando:
```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ B │ C# │ D#  │ E  │ F# │ G# │ A#  │
└───┴────┴─────┴────┴────┴────┴─────┘
```

## Mais informações sobre o CLI

Para descobrir mais opções, você pode usar a flag `--help`:
```bash
poetry run escalas --help
                                                                                       
Usage: escalas [OPTIONS] [TONICA] [TONALIDADE]                                        
                                                                                       
╭─ Arguments ─────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica da escala [default: c]                       │
│   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior]               │
╰─────────────────────────────────────────────────────────────────────────────────────╯

```