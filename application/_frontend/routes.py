from flask import Blueprint
from flask import render_template

urls_frontend = Blueprint('frontend', __name__,)

@urls_frontend.route('/')
def home():
    return render_template('public/home.html')

@urls_frontend.app_errorhandler(404)
def handle_404(error):
    return render_template('public/error404.html'), 404

@urls_frontend.app_errorhandler(500)
def handle_500(error):
    return render_template('public/error500.html'), 500