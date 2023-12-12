from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    current_app,
)
from sqlalchemy.exc import IntegrityError

from application import db
from application.models import User
from application.users.forms import RegisterForm, LoginForm, EmailForm, PasswordForm
from flask_login import login_user, login_required, logout_user, current_user

users_blueprint = Blueprint("users", __name__, template_folder="templates/users")


@users_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                new_user = User(
                    form.first_name.data,
                    form.last_name.data,
                    form.email.data,
                    form.password.data,
                )
                db.session.add(new_user)
                db.session.commit()
                current_app.logger.info(f"Registered new user: {form.email.data}!")
                flash("Thank you for registering!")

                return redirect(url_for("users.login"))
            except IntegrityError:
                db.session.rollback()
                current_app.logger.error(f"Error registering user: {form.email.data}!")
                flash("Issue registering your account, email already registered")
        else:
            flash("Please check you entered you information correctly")

    return render_template("register.html", form=form)


@users_blueprint.route("/password_reset")
def password_reset():
    return render_template("password_reset.html")


@users_blueprint.route("/logout")
@login_required
def logout():
    current_app.logger.info(f"User logged out: {current_user.email}")
    logout_user()

    flash("You have been logged out.")
    return redirect(url_for("main.index"))


@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if current_user.is_authenticated:
            current_app.logger.info(f"User already logged in: {current_user.email}")
            flash("Already logged in!")
            return redirect(url_for("users.profile"))

    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()

            if user is not None and user.password_correct(form.password.data):
                login_user(user)
                current_app.logger.info(f"User logged in: {current_user.email}")
                flash("Login Successful")

                return redirect(url_for("users.profile"))

    return render_template("login.html", form=form)


@users_blueprint.route("/profile")
@login_required
def profile():
    return render_template("profile.html")
