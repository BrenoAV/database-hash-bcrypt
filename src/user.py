from dataclasses import dataclass

import bcrypt


@dataclass
class User:
    username: str
    email: str
    password: str

    def __post_init__(self):
        if not isinstance(self.username, str):
            raise TypeError("username should be of type str")
        if not isinstance(self.email, str):
            raise TypeError("email should be of type str")
        if not isinstance(self.password, str):
            raise TypeError("password should be of type str")

        # Hashing the password
        self.password = self.generate_hash_password(self.password)

    @staticmethod
    def generate_hash_password(passwd: str) -> str:
        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password=passwd.encode(), salt=salt)
        return hashed.decode("utf-8")
