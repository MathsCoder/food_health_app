from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Integer, String, DateTime
from flask_login import UserMixin
from application import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


###################
# Database Models #
###################


class User(db.Model, UserMixin):
    """
    Class for user model representing a user in the database.

    Attributes:
    - id: Unique identifier for the user, the primary key in the database.
    - first_name: String field to store the user's first name.
    - last_name: String field to store the user's last name.
    - email: Unique and non-nullable string field for the user's email address.
    - hashed_password: String field to store the hashed password.
    - registration_date: DateTime field to store the user's registration date and time.
                         It defaults to the current UTC time when the user is created.
    """

    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String)
    last_name = db.Column(String)
    email = db.Column(String, unique=True, nullable=False)
    hashed_password = db.Column(String(200), nullable=False)
    registration_date = db.Column(DateTime, nullable=False, default=datetime.utcnow)

    images = db.relationship("UploadImage", backref="uploader", lazy=True)

    def __init__(self, first_name, last_name, email, non_hashed_password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hashed_password = generate_password_hash(non_hashed_password)
        self.registration_date = datetime.utcnow()

    def password_correct(self, non_hashed_password):
        return check_password_hash(self.hashed_password, non_hashed_password)

    def __repr__(self):
        return f"Name: {self.name} | Email: {self.email}"


class UploadImage(db.Model):
    """
    Class for the image model representing an image in the database.

    Attributes:
    - id: Unique identifier for the image, the primary key in the database.
    - filename: String field to store the filename of the image
    - file_path: String field to store the path of the image file
    - uploaded_time: DateTime field to store the time when the image was uploaded.
    - user_id: Integer field that acts as a foreign key linking the image to a user.

    Relationships:
    - user: Establishes a relationship between the Image and User models.
            This allows for accessing the user who uploaded the image through the 'user' attribute.
            The backref 'images' creates a reverse relationship where a User instance can access
            all its associated Image instances.
    """

    # uploader = db.relationship(User)

    id = db.Column(Integer, primary_key=True)
    filename = db.Column(String(255), nullable=False)
    file_path = db.Column(String(255), nullable=False)
    classification = db.Column(String(50), nullable=False)
    uploaded_time = db.Column(DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, filename, file_path, user_id, classification=""):
        self.filename = filename
        self.file_path = file_path
        self.user_id = user_id
        self.classification = classification
        self.uploaded_at = datetime.now()

    def __repr__(self):
        return f"<Image: {self.filename}>"
