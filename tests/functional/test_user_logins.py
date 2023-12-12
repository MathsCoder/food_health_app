def test_login_page(test_client):
    """
    Checks the index page is returned correctly
    """

    response = test_client.get("/users/login")
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_login_successful(test_client, register_test_user):
    """
    Checks that a user with valid credentials can log in successfully.
    """

    response = test_client.post(
        "/users/login",
        data={"email": "john@example.com", "password": "password"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"User Profile" in response.data
    assert b"John" in response.data


######################
# Invalid Cases: #####
######################


def test_invalid_email(test_client, register_test_user):
    """
    Checks that a user with invalid email cannot log in.
    """
    response = test_client.post(
        "/users/login",
        data={"email": "NOTjohn@example.com", "password": "password"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_incorrect_password(test_client, register_test_user):
    """
    Checks that a user with invalid password cannot log in.
    """
    response = test_client.post(
        "/users/login",
        data={"email": "john@example.com", "password": "NOTpassword"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


# Empty Email or Password: Try to log in with one or both fields empty.
def test_empty_email(test_client, register_test_user):
    """
    Checks that an empty email cannot log in.
    """
    response = test_client.post(
        "/users/login",
        data={"email": "", "password": "password"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_empty_password(test_client, register_test_user):
    """
    Checks that an empty password cannot log in.
    """
    response = test_client.post(
        "/users/login",
        data={"email": "john@example.com", "password": ""},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data
