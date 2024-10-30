from flask import Blueprint, render_template
from flask_login import login_required, current_user

faq_page = Blueprint ('faq_page', __name__, template_folder='/templates')
@faq_page.route ('/faq', methods = ['GET'])
@login_required
def forum ():
    return render_template ("faq.html", user=current_user)