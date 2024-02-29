import argparse
import os
import sys

root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root)

from src.database import db_connection, verify_username_password


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Feed postgres database")
    parser.add_argument(
        "-u", "--username", type=str, required=True, help="your username"
    )
    parser.add_argument(
        "-p", "--password", type=str, required=True, help="your password"
    )
    return parser.parse_args()


def main():
    """Main Function"""
    args = get_args()
    conn = db_connection(
        host="localhost", port="5432", dbname="db", user="postgres", password="postgres"
    )
    if verify_username_password(
        conn=conn, username=args.username, passwd=args.password
    ):
        print("Login succefully!")
    else:
        print("Login Failed! Check the username and password =)")


if __name__ == "__main__":
    main()
