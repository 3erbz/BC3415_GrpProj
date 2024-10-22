from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import speech_recognition as sr
import textblob

explore_page= Blueprint ('explore_page', __name__, template_folder='/templates')

@explore_page.route ('/explore', methods = ['GET'])
@login_required
def explore ():
    return render_template ("explore.html", user=current_user)

@explore_page.route ('/explore/result', methods=['GET', 'POST'])
@login_required
def explore_result ():
    data_received = {}       
    if request.method == 'POST':
        # receiving data
        text_data = request.form.get('text_data')
        speech_data = request.form.get ('speech_data')
        audio_data = request.files ['audio_data']           

        # append data to dictionary
        if text_data != "":
            data_received ["text"] = text_data
        
        if audio_data.filename != "":
            # convert audio to text
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile (audio_data)
            with audioFile as source:
                data = recognizer.record(source)
            audio_data = recognizer.recognize_google (data, key=None)
            data_received ["audio"] = audio_data
            # maybe can use google genai, would require api key to be kept in environment
        
        if speech_data != "":
            data_received ["speech"] = speech_data
        
    # analysing data
    analysis_data = {}
    for data, content in data_received.items ():
        if content == None or content != "":
            analysis = textblob.TextBlob (content).sentiment
            analysis_data [data] = {"polarity": analysis.polarity, "subjectivity": analysis.subjectivity}
        
    return render_template ("explore_result.html",user=current_user,
                            data_received=data_received, 
                            analysis_data=analysis_data)