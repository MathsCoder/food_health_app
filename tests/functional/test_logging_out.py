# ------------------------- #


# Successful Logout: Ensure that a logged-in user can log out successfully.
def test_logout_page_when_logged_in(test_client, login_test_user):
    """
    Checks the index page is returned correctly
    """

    response = test_client.get("/users/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"Register Here!" in response.data


######################
# Invalid Cases: #####
######################


def test_access_denied_after_logout(test_client, login_test_user):
    """
    Checks that a user cannot access the profile page after logging out.
    """

    response = test_client.get("/users/profile", follow_redirects=True)
    assert response.status_code == 200
    assert b"Profile" in response.data
    assert b"John" in response.data

    response = test_client.get("/users/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"Register Here!" in response.data

    response = test_client.get("/users/profile", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_logout_page_when_not_logged_in(test_client):
    """
    Checks the index page is returned correctly
    """

    response = test_client.get("/users/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"Please log in to access this page." in response.data
