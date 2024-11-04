from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from website.pages.gemini_functions import chatbot_reply

faq_page = Blueprint ('faq_page', __name__, template_folder='/templates')
@faq_page.route ('/faq', methods = ['GET'])
@login_required
def faq ():
    return render_template ("faq.html", user=current_user)

@faq_page.route ('/faq/ask', methods = ['POST'])
@login_required
def ask ():
    user_input = request.json.get('question')
    response = chatbot_reply (user_input)
    return jsonify({"response": response})