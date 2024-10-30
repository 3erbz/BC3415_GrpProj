from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user



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
        # import packages
        import speech_recognition as sr
        from website.pages.scam_detection import vectorizer_predict, texblob_predict, gemini_predict

        # receiving data
        text_data = request.form.get('text_data')
        speech_data = request.form.get ('speech_data')
        audio_data = request.files ['audio_data']    

        # checking if data is valid
        if text_data == "" and audio_data.filename == "" and speech_data == "":
            flash ('Please provide either speech, text or audio data.', category='error')
            return redirect (url_for('explore_page.explore'))       

        # append data to dictionary
        if text_data != "":
            data_received ["Text"] = text_data
        
        if audio_data.filename != "":
            # convert audio to text
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile (audio_data)
            with audioFile as source:
                data = recognizer.record(source)
            audio_data = recognizer.recognize_google (data, key=None)
            data_received ["Audio"] = audio_data
            # maybe can use google genai, would require api key to be kept in environment
        
        if speech_data != "":
            data_received ["Speech"] = speech_data
        
    # analysing data using textblob
    analysis_data = texblob_predict(data_received)
        
    # Spam Detection (using the trained model)
    spam_results = vectorizer_predict (data_received)
    # scam detection using gemini
    gemini_results = gemini_predict (data_received)

    # Render the results in explore_result.html
    return render_template("explore_result.html", user=current_user,
                           data_received=data_received,
                           analysis_data=analysis_data,
                           spam_results=spam_results,
                           gemini_results=gemini_results)