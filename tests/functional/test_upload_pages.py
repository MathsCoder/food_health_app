def test_get_upload_image_page_logged_in(test_client, login_test_user):
    """
    Checks the index page is returned correctly
    """

    response = test_client.get("/upload/upload_image")
    assert response.status_code == 200
    assert b"Upload Image" in response.data


def test_post_upload_image_when_logged_in_successful(test_client, login_test_user):
    """
    Checks uploading an image when logged in is successful
    """
    pass


######################
# Invalid Cases: #####
######################


def test_get_upload_image_page_when_not_logged_in(test_client):
    """
    Checks the index page is returned correctly
    """

    response = test_client.get("/upload/upload_image", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data
