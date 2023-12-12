from application.models import User


def test_get_register_page(test_client):
    """
    Checks the index page is returned correctly
    """

    response = test_client.get("/users/register")
    assert response.status_code == 200
    assert b"User Registration" in response.data
    assert b"First Name" in response.data
    assert b"Last Name" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_register_successful(test_client):
    """
    Checks the registration is successful
    """

    response = test_client.post(
        "/users/register",
        data={
            "first_name": "John",
            "last_name": "Smith",
            "email": "Another_john@example.com",
            "password": "password",
            "confirm": "password",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert User.query.filter_by(email="Another_john@example.com").first() is not None


######################
# Invalid Cases: #####
######################


def test_invalid_email_format(test_client):
    """
    Checks the registration is unsuccessful
    """

    response = test_client.post(
        "/users/register",
        data={
            "first_name": "John",
            "last_name": "Smith",
            "email": "johnexample.com",
            "password": "password",
            "confirm": "password",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Please check you entered you information correctly" in response.data


def test_duplicate_register_unsuccessful(test_client, register_test_user):
    """
    Checks the registration is unsuccessful
    """

    response = test_client.post(
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
    assert response.status_code == 200
    assert b"Issue registering your account, email already registered" in response.data
