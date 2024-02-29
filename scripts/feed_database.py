import argparse
import os
import sys

root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root)

from src.database import db_connection, insert_database
from src.user import User


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Feed postgres database")
    parser.add_argument(
        "-u",
        "--username",
        type=str,
        required=True,
        help="an username for the application",
    )
    parser.add_argument(
        "-p",
        "--password",
        type=str,
        required=True,
        help="a password for the application",
    )
    parser.add_argument(
        "-e", "--email", type=str, required=True, help="an e-mail for the application"
    )
    return parser.parse_args()


def main():
    """Main Function"""
    args = get_args()
    conn = db_connection(
        host="localhost", port="5432", dbname="db", user="postgres", password="postgres"
    )
    # Insert a record in the Database
    insert_database(
        conn,
        user=User(username=args.username, email=args.email, password=args.password),
    )


if __name__ == "__main__":
    main()
