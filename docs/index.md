# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

[Index](./source/app.md)

## Listas

### Não ordenadas

- X
- Y
- Z

### Ordenadas

1. Primeiro
2. Segundo
3. Terceiro

## Alterações de texto

**Negrito**

*italico*

`segredo = 42`

Emoji - :snake: :heart: :rocket:

~~Tachado~~

==Realçado==

## Citações

Alguém disse

> Essa é uma citação

## Link

[DuckDuckGo](http://ddg.gg)

## Tabela

| Nome | Idade |
| ---- | ----- |
| Eduardo | 28 |
| Fausto  | 04 |

## Lista de tarefas

- [ ] Dar like no vídeo
- [ ] Se increver no canal
- [x] Assistir a live de mkdocs

## Bloco de código

```{.py3 hl_lines="1 3" linenums="55" title="meu_arquivo.py"}
def xpto():
   """Docstring."""
   return True
```

## Custom fences
```mermaid
flowchart LR
    A --o B
    B --x C