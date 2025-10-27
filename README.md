# 🤖 Automação de E-mail e Processamento de Boletos

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)](https://www.python.org/) [![FreeSimpleGUI 5.0+](https://img.shields.io/badge/FreeSimpleGUI-5.0%2B-brightgreen)](#) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

_*Sistema automatizado para download de anexos de e-mail e extração de dados de boletos.*_

---

# Importando-bibliotecas

Uma coleção de pequenos exemplos em Python criados enquanto eu aprendia a trabalhar com bibliotecas comuns do ecossistema. O objetivo deste repositório é servir como referência prática e didática — scripts simples e comentados que mostram como usar módulos como `random`, `datetime`, `tkinter` e `xlwings`.

## Conteúdo do repositório

- `Exemplos/Aprendendo a usar uma biblioteca com random.py` — exemplo simples de geração de números aleatórios.
- `Exemplos/Datetime saudações.py` — script que exibe uma saudação apropriada conforme a hora do dia e imprime a data/hora atual.
- `Exemplos/Janela Simples com Tkinter.py` — exemplo básico de interface gráfica usando `tkinter`.
- `Exemplos/Manipulando Excel com xlwings.py` — demonstração de leitura de formatação (cor de fundo) de célula no Excel usando `xlwings`.

## Principais características

- Exemplos curtos e focados, fáceis de entender.
- Comentários explicativos em cada exemplo.
- Pronto para executar no Windows (alguns exemplos dependem do Excel/Windows).

## Dependências

- Python 3.8+ (recomendado)
- `xlwings` (apenas para o exemplo que manipula Excel)
- `tkinter` normalmente já vem com o Python em instalações padrão.

Observação: o exemplo com `xlwings` exige Microsoft Excel instalado no Windows e pode requerer permissões/ajustes adicionais (como instalar `pywin32`) dependendo do ambiente.

## Instalação (rápida)

No Windows (cmd.exe):

```bat
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install xlwings
```

Se preferir, instale apenas as dependências necessárias caso vá usar apenas alguns exemplos:

```bat
pip install xlwings
```

## Como executar os exemplos

Abra o terminal (cmd.exe) na pasta do repositório e execute o script desejado. Exemplos:

```bat
python "Exemplos\Datetime saudações.py"
python "Exemplos\Aprendendo a usar uma biblioteca com random.py"
python "Exemplos\Janela Simples com Tkinter.py"
python "Exemplos\Manipulando Excel com xlwings.py"
```

Observações:
- O `Manipulando Excel com xlwings.py` cria/abre um arquivo Excel e usa a API do Excel; execute com o Excel instalado.
- O `Tkinter` abre uma janela gráfica — execute em um ambiente com suporte a GUI.

## Exemplos rápidos

- O exemplo `Datetime saudações` demonstra como obter a hora atual e escolher uma saudação adequada (manhã/tarde/noite/madrugada).
- O exemplo `random` mostra como gerar números inteiros aleatórios com `randint`.

## Contribuindo

Contribuições são bem-vindas. Sugestões:

1. Abra uma issue descrevendo a melhoria ou correção.
2. Faça um fork, crie uma branch com a sua mudança e abra um pull request com uma descrição clara.

Por favor, mantenha os exemplos pequenos, com código legível e comentado.

## Licença

Este repositório está sob a licença descrita no arquivo `LICENSE`.

## Contato

Criador: Felipe Alcantara

Para dúvidas ou sugestões: abra uma issue neste repositório.

---

Obrigado por conferir o repositório — use os exemplos como ponto de partida para seus próprios projetos em Python.
