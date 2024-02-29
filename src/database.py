import bcrypt
import psycopg2

from src.user import User


def db_connection(
    host: str, port: str, dbname: str, user: str, password: str
) -> psycopg2.extensions.connection:
    return psycopg2.connect(
        f"host={host} port={port} dbname={dbname} user={user} password={password}"
    )


def insert_database(conn: psycopg2.extensions.connection, user: User) -> None:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
        (user.username, user.email, user.password),
    )
    conn.commit()


def verify_username_password(
    conn: psycopg2.extensions.connection, username: str, passwd: str
) -> bool:
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    if isinstance(result, tuple):
        return bcrypt.checkpw(
            password=passwd.encode(), hashed_password=result[0].encode()
        )
    return False
