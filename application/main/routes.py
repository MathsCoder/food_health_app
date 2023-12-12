from flask import Blueprint, render_template

# Register the Blueprint with the Flask application instance (app)
main_blueprint = Blueprint("main", __name__, template_folder="templates/main")


@main_blueprint.route("/")
def index():
    return render_template("index.html")


@main_blueprint.app_errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@main_blueprint.app_errorhandler(403)
def page_forbidden(error):
    return render_template("403.html"), 403
