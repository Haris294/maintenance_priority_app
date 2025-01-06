from flask import Flask, request, jsonify
import joblib
import logging

# Initialize Flask App
app = Flask(__name__)

# Load model and encoders
try:
    model = joblib.load('app/models/maintenance_model.pkl')
    vectorizer = joblib.load('app/models/vectorizer.pkl')
    label_encoder = joblib.load('app/models/label_encoder.pkl')
except FileNotFoundError as e:
    logging.error(f"Model files not found: {e}")
    exit(1)

@app.route('/')
def home():
    return "Flask app is running! Use the /classify endpoint with a POST request."

@app.route('/classify', methods=['POST'])
def classify():
    try:
        data = request.json
        user_request = data.get('request', '')

        if not user_request:
            return jsonify({'error': 'No maintenance request provided'}), 400

        # Predict priority
        input_vector = vectorizer.transform([user_request])
        prediction = model.predict(input_vector)
        category = label_encoder.inverse_transform(prediction)[0]

        return jsonify({'priority': category})
    except Exception as e:
        logging.error(f"Error during classification: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
