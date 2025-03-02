from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import pickle
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load your model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return "Welcome to the Trading Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data['feature1'], data['feature2']]
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
