from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the model
with open('spam_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a route for the root URL
@app.route('/')
def home():
    return "Welcome to the Spam Email Detector API!"

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        message = data['message']
        prediction = model.predict([message])[0]
        return jsonify({'prediction': 'spam' if prediction == 1 else 'ham'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)