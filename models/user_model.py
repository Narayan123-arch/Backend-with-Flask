from db import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS nuser(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(50),
            password TEXT
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM nuser")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users


def insert_user(name, email, password=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO nuser (name,email,password) VALUES (%s,%s,%s)",
        (name, email, password)
    )
    conn.commit()
    cur.close()
    conn.close()


def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM nuser WHERE id=%s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()