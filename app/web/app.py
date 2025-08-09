from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(
            dbname="appdb",
            user="appuser",
            password="apppass",
            host="db",
            port=5432
        )
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM visitas;")
        count = cur.fetchone()[0]
        cur.execute("INSERT INTO visitas DEFAULT VALUES;")
        conn.commit()
        cur.close()
        conn.close()
        return f"Visitas: {count + 1}"
    except Exception as e:
        return f"Erro: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
