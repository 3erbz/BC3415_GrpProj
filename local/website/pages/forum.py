from flask import Blueprint, render_template
from flask_login import login_required, current_user

forum_page = Blueprint ('forum_page', __name__, template_folder='/templates')
@forum_page.route ('/forum', methods = ['GET'])
@login_required
def forum ():
    return render_template ("forum.html", user=current_user)
