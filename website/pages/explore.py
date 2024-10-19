from flask import Blueprint, render_template
from flask_login import login_required, current_user

explore_page= Blueprint ('explore_page', __name__, template_folder='/templates')

@explore_page.route ('/explore', methods = ['GET'])
@login_required
def explore ():
    return render_template ("explore.html", user=current_user)


@explore_page.route ('/explore/result', methods = ['GET'])
@login_required
def result ():
    return render_template ("explore_result.html", user=current_user)
