import os
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    send_from_directory,
    current_app,
)
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError

from .image_processor import process_image
from .image_classifier import classify_image
from application.uploads.forms import ImageUploadForm
from application.models import UploadImage
from application import db


upload_blueprint = Blueprint("upload", __name__, template_folder="templates/uploads")


@upload_blueprint.route("/upload_image", methods=["GET", "POST"])
@login_required
def upload_image():
    form = ImageUploadForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if form.image.data:
                image = process_image(form.image.data, current_user.get_id())
                label = classify_image(image[1])
            new_image = UploadImage(image[0], image[1], current_user.get_id(), label)
            try:
                db.session.add(new_image)
                db.session.commit()
                flash("Image uploaded")
                current_app.logger.info(f"New image uploaded: {new_image.filename}")
                return redirect(url_for("upload.view_uploads"))
            except IntegrityError:
                db.session.rollback()
                current_app.logger.error(f"Error uploading image: {new_image.filename}")
                flash("Image with same name already uploaded")

        else:
            flash("Please try uploading the image again")

    return render_template("upload_image.html", form=form)


@upload_blueprint.route("/my_food")
@login_required
def view_uploads():
    images = UploadImage.query.filter_by(user_id=current_user.id).all()
    current_app.logger.info(f"Viewing images for user: {current_user.id}")
    return render_template("my_food.html", images=images)


@upload_blueprint.route("/")
def get_images(filename):
    path = os.path.join(current_app.root_path, "image_uploads/food")
    return send_from_directory(path, filename)
