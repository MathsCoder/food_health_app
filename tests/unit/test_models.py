def test_new_user(new_user):
    """
    Test that a new user is created correctly, with the correct details.
    """
    assert new_user.first_name == "John"
    assert new_user.last_name == "Smith"
    assert new_user.email == "john@example.com"
    assert new_user.hashed_password != "password"


def test_new_image(new_image):
    """
    Test that a new image is created correctly, with the correct details.
    """
    assert new_image.filename == "test.jpg"
    assert new_image.file_path == "/test/test.jpg"
    assert new_image.user_id == 1
