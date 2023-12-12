from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import ValidationError
from application.models import User


#########
# Forms #
#########


class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=1)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=1)])
    email = StringField(
        "Email", validators=[DataRequired(), Email(), Length(min=6, max=100)]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            EqualTo("confirm", "Passwords must match"),
            Length(min=8, max=100),
        ],
    )
    confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def is_email_already_registered(self):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError("This email has already been registered.")


class LoginForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email(), Length(min=6, max=100)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=100)]
    )
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")


class EmailForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email(), Length(min=6, max=100)]
    )
    submit = SubmitField("Register")


class PasswordForm(FlaskForm):
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=100)]
    )
    submit = SubmitField("Register")
