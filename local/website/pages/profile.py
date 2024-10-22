from flask import Blueprint, render_template
from flask_login import login_required, current_user

profile_page = Blueprint ('profile_page', __name__, template_folder='/templates')

@profile_page.route ('/profile', methods = ['GET'])
@login_required
def rewards ():
    return render_template ("profile.html", user=current_user)