from flask import Flask, request, jsonify, render_template
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

# Frontend: Input form
@app.route('/')
def home():
    return render_template('index.html')

# Frontend: Handle form submission
@app.route('/result', methods=['POST'])
def result():
    data = request.form.get('request')  # Get the input from the form
    if not data:
        return render_template('index.html', error="Please provide a maintenance request.")

    try:
        # Process the input and predict
        input_vector = vectorizer.transform([data])
        prediction = model.predict(input_vector)
        category = label_encoder.inverse_transform(prediction)[0]

        # Render the result
        return render_template('result.html', request=data, priority=category)
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        return render_template('index.html', error="Internal Server Error")


# API: JSON-based classification
@app.route('/api/classify', methods=['POST'])
def classify():
    data = request.json
    user_request = data.get('request', '')

    if not user_request:
        return jsonify({'error': 'No maintenance request provided'}), 400

    try:
        # Predict priority
        input_vector = vectorizer.transform([user_request])
        prediction = model.predict(input_vector)
        category = label_encoder.inverse_transform(prediction)[0]
        return jsonify({'priority': category})
    except Exception as e:
        logging.error(f"Error occurred during prediction: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
