import bcrypt
import pytest

from src.user import User


def test_user_created_success():
    name = "Breno"
    email = "breno@example.com"
    password = "my@password"
    user = User(username=name, email=email, password=password)
    assert user.username == name
    assert user.email == email
    assert bcrypt.checkpw(
        password=password.encode(), hashed_password=user.password.encode()
    )


def test_user_missing_params():
    with pytest.raises(TypeError) as exc_info:
        _ = User(username=123, email="breno@example.com", password="123")
    assert str(exc_info.value) == "username should be of type str"
    with pytest.raises(TypeError) as exc_info:
        _ = User(username="Breno", email=123, password="123")
    assert str(exc_info.value) == "email should be of type str"
    with pytest.raises(TypeError) as exc_info:
        _ = User(username="Breno", email="breno@example.com", password=123)
    assert str(exc_info.value) == "password should be of type str"
