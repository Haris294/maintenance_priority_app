from flask import Flask, request, jsonify, render_template, redirect, url_for
import joblib
import logging

app = Flask(__name__)

# Load the model and encoders
try:
    model = joblib.load('app/models/maintenance_model.pkl')
    vectorizer = joblib.load('app/models/vectorizer.pkl')
    label_encoder = joblib.load('app/models/label_encoder.pkl')
except FileNotFoundError as e:
    logging.error(f"Model files not found: {e}")
    exit(1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    user_request = request.form.get('request', '').strip()

    if not user_request:
        return render_template('index.html', error="Please provide a maintenance request!")

    try:
        # Predict priority
        input_vector = vectorizer.transform([user_request])
        prediction = model.predict(input_vector)
        category = label_encoder.inverse_transform(prediction)[0]

        return render_template('result.html', priority=category, request=user_request)
    except Exception as e:
        logging.error(f"Error occurred during prediction: {str(e)}")
        return render_template('index.html', error="Internal Server Error. Please try again later.")

if __name__ == '__main__':
    app.run(debug=True)
