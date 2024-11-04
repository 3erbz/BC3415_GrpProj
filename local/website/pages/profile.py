from flask import Blueprint, render_template
from flask_login import login_required, current_user
from website.models import Scams

profile_page = Blueprint ('profile_page', __name__, template_folder='/templates')

@profile_page.route ('/profile', methods = ['GET'])
@login_required
def profile ():
    user_id = current_user.id
    scams = Scams.query.filter_by (user_id=user_id).count ()

    # log data
    scam_data = Scams.query.filter_by (user_id=user_id).all ()
    
    return render_template ("profile.html", 
                            user=current_user,
                            scams=scams,
                            scam_data=scam_data)