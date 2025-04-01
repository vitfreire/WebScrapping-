import sqlite3
import asyncio
from playwright.async_api import async_playwright

# Função principal

async def raspar_site():
    # Conectar ao banco SQLite
    conn = sqlite3.connect("nahora.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            data TEXT,
            conteudo TEXT
        )
    """)

    async with async_playwright() as p:
        # headless=True = sem abrir janela
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("http://nahoradoocio.lowlevel.com.br/", timeout=60000)

        # Esperar os posts aparecerem
        await page.wait_for_selector("article")

        # Capturar os artigos
        artigos = await page.query_selector_all("article")

        print(f"{len(artigos)} posts encontrados.")

        for artigo in artigos:
            try:
                titulo = await artigo.query_selector("h2")
                data = await artigo.query_selector(".date")
                conteudo = await artigo.query_selector(".entry")

                titulo_texto = await titulo.inner_text() if titulo else ""
                data_texto = await data.inner_text() if data else ""
                conteudo_texto = await conteudo.inner_text() if conteudo else ""

                cursor.execute(
                    "INSERT INTO posts (titulo, data, conteudo) VALUES (?, ?, ?)",
                    (titulo_texto.strip(), data_texto.strip(), conteudo_texto.strip())
                )
            except Exception as e:
                print("Erro ao extrair artigo:", e)

        await browser.close()
        conn.commit()
        conn.close()
        print("Dados inseridos com sucesso.")

# Executar a função assíncrona
asyncio.run(raspar_site())
