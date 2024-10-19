from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import textblob

explore_page= Blueprint ('explore_page', __name__, template_folder='/templates')

@explore_page.route ('/explore', methods = ['GET'])
@login_required
def explore ():
    return render_template ("explore.html", user=current_user)


@explore_page.route ('/process', methods = ['GET','POST'])
def process_data ():   
    data  = request.form.get('data')
    res = data.upper()
    return res

# @explore_page.route ('/explore/result', methods = ['GET','POST'])
# def process_data2 ():   
#     data  = request.form
#     return render_template ("explore_result.html", user=current_user)