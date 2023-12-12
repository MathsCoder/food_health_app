from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class ImageUploadForm(FlaskForm):
    """
    Form for uploading an image.

    Attributes:
    - image: Field for the image file.
    """

    image = FileField(
        "Upload Image",
        validators=[
            FileRequired(),
            FileAllowed(
                ["jpg", "jpeg", "png"], "Only jpg, jpeg, and png filetypes accepted"
            ),
        ],
    )
    submit = SubmitField("Upload Image")
