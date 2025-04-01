import sqlite3


def verificar_dados():
    try:
        conn = sqlite3.connect("nahora.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, titulo, data FROM posts ORDER BY id DESC")
        registros = cursor.fetchall()

        if not registros:
            print("Nenhum dado encontrado na tabela 'posts'.")
        else:
            for r in registros:
                print(f"ID: {r[0]} | Título: {r[1]} | Data: {r[2]}")

    except sqlite3.Error as e:
        print("Erro ao acessar o banco:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    verificar_dados()
