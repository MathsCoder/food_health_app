########################
# Tests for user pages #
########################
def test_get_index_page(test_client):
    """
    Checks the index page is returned correctly
    """

    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Food App" in response.data
    assert b"Register Here!" in response.data


def test_profile_page_logged_in(test_client, login_test_user):
    """
    Checks the index page is returned correctly
    """

    response = test_client.get("/users/profile")
    assert response.status_code == 200
    assert b"Profile" in response.data
    assert b"John" in response.data


def test_forgot_password_page(test_client):
    """
    Checks the index page is returned correctly
    """

    response = test_client.get("/users/password_reset")
    assert response.status_code == 200


#######################################################################
# Tests for user pages which require login when user is not logged in #
#######################################################################
def test_profile_page_not_logged_in(test_client):
    """
    Checks the index page is returned correctly
    """

    response = test_client.get("/users/profile", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data
