def chatbot_reply (question, user_id):
    import google.generativeai as genai
    from dotenv import load_dotenv
    from pathlib import Path
    import os   
    from website.models import FAQ, Chatbot
    from website import db

    env_path = Path('.')/'.env'
    load_dotenv (dotenv_path=env_path)
    api_key = os.environ.get('GEMINI_API_KEY')
    genai.configure(api_key=api_key)

    # Set up chat session with initial history
    history = []
    faq = FAQ.query.filter_by (user_id=user_id).all()
    for item in faq:
        user = {"role": "user", "parts": [item.user_response]}
        history.append(user)

    chatbot = Chatbot.query.filter_by (user_id=user_id).all()
    for item in chatbot:
        model = {"role": "model", "parts": [item.chatbot_response]}
        history.append(model)

    # Create the model
    generation_config = {
    "temperature": 1.2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 500,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You should be knowledgeable about various types of scams such as phishing, identity theft, fake investment schemes, and fraudulent loan offers. The chatbot should provide clear, accurate, and reassuring responses, educating users on how to identify scams, avoid common pitfalls, and respond safely if they suspect they’ve encountered a scam. Additionally, you should be able to provide general tips on financial safety and staying secure online. Ensure that the tone is friendly, trustworthy, and easy to understand.",
    )

    chat_session = model.start_chat(
    history=history
    )

    response = chat_session.send_message(question)
    response = response.text

    # send user response to datbase
    user_question = FAQ(user_response=question, user_id=user_id)
    db.session.add(user_question)
    db.session.commit()

    # send chatbot response to datbase
    chatbot_response = Chatbot(chatbot_response=response, user_id=user_id)
    db.session.add(chatbot_response)
    db.session.commit()

    return response

def comment_reply (comment, thread_id):
    from website.models import Comment, GeminiComment
    import google.generativeai as genai
    from dotenv import load_dotenv
    from pathlib import Path
    import os   

    env_path = Path('.')/'.env'
    load_dotenv (dotenv_path=env_path)
    api_key = os.environ.get('GEMINI_API_KEY')
    genai.configure(api_key=api_key)

    # create chat history
    history=[]
    comments = Comment.query.filter_by (thread_id=thread_id).all ()
    for item in comments:
        user = {"role": "user", "parts" :[item.comment]}
        history.append(user)

    gemini_replies  = GeminiComment.query.filter_by (thread_id=thread_id).all ()
    for item in gemini_replies:
        model = {"role": "model", "parts" :[item.response]} 
        history.append(model)

    print (history)

    # Create the model
    generation_config = {
    "temperature": 1.2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="To provide effective forum responses, stay concise, relevant, and friendly. Acknowledge the user's perspective, then respond directly to key points, using examples where helpful. Keep a neutral, respectful tone, especially on sensitive topics, and encourage further engagement with follow-up questions or additional resources. Adapt language to suit the audience, and proofread for clarity and professionalism before posting. This approach keeps discussions informative and engaging while fostering a positive community atmosphere.",
    )

    chat_session = model.start_chat(
        history=history
    )

    response = chat_session.send_message(comment)
    response = response.text

    return response

def summarise (data):
    import google.generativeai as genai
    from dotenv import load_dotenv
    from pathlib import Path
    import os   

    env_path = Path('.')/'.env'
    load_dotenv (dotenv_path=env_path)
    api_key = os.environ.get('GEMINI_API_KEY')
    genai.configure(api_key=api_key)

    # Create the model
    model = genai.GenerativeModel ("gemini-1.5-flash")
    prompt = "Categorise the gist in less than 5 words without any indication of whether it is a scam or not: " + data
    response = model.generate_content (prompt)
    response = response.text

    return response