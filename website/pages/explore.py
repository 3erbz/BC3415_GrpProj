from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

explore_page= Blueprint ('explore_page', __name__, template_folder='/templates')

@explore_page.route ('/explore', methods = ['GET'])
@login_required
def explore ():
    return render_template ("explore.html", user=current_user)

@explore_page.route ('/explore/result', methods=['GET', 'POST'])
@login_required
def explore_result ():
    if request.method == 'POST':
        final_data  = {}
        # register data
        text_data = request.form['text_data']
        speech_data = request.form.get ('speech_data')

        print (speech_data)

        # append data to dictionary
        final_data ["text"] = text_data
        final_data ["speech"] = speech_data

        # process data and generate response data
        res_data = {}
        import textblob
        for data, content in final_data.items ():
            if content != None:
                analysis = textblob.TextBlob (content).sentiment
                res_data [data] = {"polarity": analysis.polarity, "subjectivity": analysis.subjectivity}

        
        print (res_data)
        
        return render_template ("explore_result.html",user=current_user,data=res_data)