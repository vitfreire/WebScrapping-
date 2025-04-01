
# Projeto Integrador — Raspagem de Conteúdo com Python + Playwright

Este projeto foi desenvolvido como parte da disciplina **Projeto Integrador** do curso de **Análise e Desenvolvimento de Sistemas** do **Centro Universitário CESMAC**.

## Descrição

O objetivo do projeto é realizar a raspagem de dados do site `http://nahoradoocio.lowlevel.com.br/`, cujo conteúdo é carregado dinamicamente via JavaScript. Para isso, foi utilizada a biblioteca `Playwright` com Python, capaz de simular um navegador real e capturar informações renderizadas dinamicamente.

## Funcionalidades implementadas

- Raspagem de conteúdo (título, data e texto dos artigos)
- Renderização da página via Playwright (modo headless)
- Armazenamento dos dados em banco relacional SQLite
- Prevenção de duplicações com chave única no título
- Geração de log de execução em `log.txt`
- Organização modular com scripts separados
- Visualização dos dados por terminal com `verificar_db.py`

## Estrutura do projeto

```
projeto-integrador/
├── main.py                # raspagem e gravação no banco
├── verificar_db.py        # visualização dos dados no terminal
├── log.txt                # registro das execuções
├── nahora.db              # banco de dados SQLite
```

## Tecnologias utilizadas

- Python 3.11  
- Playwright  
- SQLite  
- Programação assíncrona com asyncio

## Instruções para execução

1. Instalar dependências:

```bash
pip install playwright
playwright install
```

2. Executar o script principal:

```bash
python main.py
```

3. Verificar os dados inseridos:

```bash
python verificar_db.py
```

## Observações

A funcionalidade de exportação para CSV e o agendamento automático ainda **não foram implementados** nesta versão.

---

## Autoras

Projeto desenvolvido por:

- Vitória Lo-ruama Gonçalves Freire  
- Luana Maria Leandro Rodrigues dos Santos  
```

