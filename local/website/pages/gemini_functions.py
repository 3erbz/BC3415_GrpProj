def chatbot_reply (question):
    import google.generativeai as genai
    from dotenv import load_dotenv
    from pathlib import Path
    import os   

    env_path = Path('.')/'.env'
    load_dotenv (dotenv_path=env_path)
    api_key = os.environ.get('GEMINI_API_KEY')
    genai.configure(api_key=api_key)

    # Set up chat session with initial history
    genai.configure(api_key=api_key)

    # Create the model
    generation_config = {
    "temperature": 1.2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-002",
    generation_config=generation_config,
    system_instruction="TTT should be knowledgeable about various types of scams such as phishing, identity theft, fake investment schemes, and fraudulent loan offers. The chatbot should provide clear, accurate, and reassuring responses, educating users on how to identify scams, avoid common pitfalls, and respond safely if they suspect they’ve encountered a scam. Additionally, TTT should be able to provide general tips on financial safety and staying secure online. Ensure TTT’s tone is friendly, trustworthy, and easy to understand.",
    )

    chat_session = model.start_chat(
    history=[{
                "role": "model",
                "parts": [
                    "Hi there! I'm TTT, your friendly guide to financial safety. I can help you understand and avoid scams related to financial institutions. What can I do for you today?"
                ],
            }
    ]
    )

    response = chat_session.send_message(question)

    return response.text

def comment_reply (comment):
    import google.generativeai as genai
    from dotenv import load_dotenv
    from pathlib import Path
    import os   

    env_path = Path('.')/'.env'
    load_dotenv (dotenv_path=env_path)
    api_key = os.environ.get('GEMINI_API_KEY')
    genai.configure(api_key=api_key)

    # Create the model
    generation_config = {
    "temperature": 1.2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-002",
    generation_config=generation_config,
    system_instruction="To provide effective forum responses, stay concise, relevant, and friendly. Acknowledge the user's perspective, then respond directly to key points, using examples where helpful. Keep a neutral, respectful tone, especially on sensitive topics, and encourage further engagement with follow-up questions or additional resources. Adapt language to suit the audience, and proofread for clarity and professionalism before posting. This approach keeps discussions informative and engaging while fostering a positive community atmosphere.",
    )

    history= []

    chat_session = model.start_chat(
        history=history
    )

    response = chat_session.send_message(comment)

    history.append({"role": "user", "parts": [comment]})
    history.append({"role": "model", "parts": [response]})

    return response.text