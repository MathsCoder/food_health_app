import os
import pytest
from application import create_app, db
from application.models import User, UploadImage


@pytest.fixture(scope="module")
def test_client():
    os.environ["FLASK_CONFIG"] = "config.TestingConfig"
    app = create_app()

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()

        yield testing_client

        with app.app_context():
            db.drop_all()


@pytest.fixture(scope="module")
def register_test_user(test_client):
    test_client.post(
        "/users/register",
        data={
            "first_name": "John",
            "last_name": "Smith",
            "email": "john@example.com",
            "password": "password",
            "confirm": "password",
        },
        follow_redirects=True,
    )


@pytest.fixture(scope="function")
def login_test_user(test_client, register_test_user):
    test_client.post(
        "/users/login",
        data={"email": "john@example.com", "password": "password"},
        follow_redirects=True,
    )
    yield

    test_client.get("/users/logout", follow_redirects=True)


@pytest.fixture(scope="module")
def new_user():
    user = User("John", "Smith", "john@example.com", "password")
    return user


@pytest.fixture(scope="module")
def new_image():
    image = UploadImage("test.jpg", "/test/test.jpg", 1)
    return image
