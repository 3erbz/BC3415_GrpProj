def gemini_reply (comment):
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