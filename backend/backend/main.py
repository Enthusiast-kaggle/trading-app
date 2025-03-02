from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load your model
model = pickle.load(open("model.pkl", "rb"))

# Home route (Root URL)
@app.route('/')
def home():
    return "Welcome to the Trading Prediction API"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data['feature1'], data['feature2']]
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


