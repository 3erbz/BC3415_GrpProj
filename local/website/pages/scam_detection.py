import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Function to load the model
def load_scam_model():
    try:
        with open('/Users/shanelim/Desktop/Sem 3.1/BC3409/Project/AISpam/website/pages/pretrained_model/saved_models/best_scam_detection_model.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

# Function to load the vectorizer
def load_vectorizer():
    try:
        with open('/Users/shanelim/Desktop/Sem 3.1/BC3409/Project/AISpam/website/pages/pretrained_model/saved_models/best_vectorizer.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

# Function to predict whether content is spam, suspicious, or not spam
def predict_scam(content):
    model = load_scam_model()
    vectorizer = load_vectorizer()

    if not model or not vectorizer:
        return "Model or vectorizer not found!"

    # Transform the content using the vectorizer
    transformed_content = vectorizer.transform([content])
    
    # Make the prediction
    prediction = model.predict(transformed_content)
    
    # Return label based on prediction
    if prediction[0] == 'scam':
        return "Scam"
    elif prediction[0] == 'legitimate':
        return "Not Scam"

