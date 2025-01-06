Maintenance Priority Classifier
A Flask-based web application and REST API that classifies maintenance requests into priority levels using a pre-trained machine learning model.

Features
Frontend: A user-friendly interface for submitting maintenance requests.
REST API: Programmatic access to classify maintenance requests.
Machine Learning Model: Predicts the priority of maintenance tasks based on the request description.
Real-time Classification: Quickly processes requests and returns priority labels like High, Medium, or Low.
Demo
Frontend

REST API
Endpoint: /api/classify

Request (JSON):
json
Copy code
{
    "request": "The AC is leaking water."
}
Response (JSON):
json
Copy code
{
    "priority": "High"
}
Installation and Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/maintenance_priority_app.git
cd maintenance_priority_app
2. Set Up a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Train the Model (Optional)
If you want to retrain the model:

bash
Copy code
python3 scripts/train_model.py
The trained model and encoders will be saved in the app/models/ directory.

5. Run the Application
bash
Copy code
python3 app/app.py
Access the app at: http://127.0.0.1:5000

Directory Structure
plaintext
Copy code
maintenance_priority_app/
│
├── app/
│   ├── templates/             # HTML files for the frontend
│   │   ├── index.html         # Input page for user requests
│   │   ├── result.html        # Display results
│   ├── static/                # Static files (CSS, images)
│   │   ├── styles.css         # Styling for the app
│   ├── app.py                 # Main application logic
│   ├── models/                # Trained model and encoders
│       ├── maintenance_model.pkl
│       ├── vectorizer.pkl
│       ├── label_encoder.pkl
│
├── scripts/                   # Machine learning scripts
│   ├── train_model.py         # Script to train and save the model
│
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
Usage Instructions
Frontend
Open your browser and go to: http://127.0.0.1:5000
Enter a maintenance request in the provided field and click "Classify".
View the priority level on the results page.
REST API
Use a tool like Postman or curl to send a POST request to:
http://127.0.0.1:5000/api/classify

Example Request:

bash
Copy code
curl -X POST http://127.0.0.1:5000/api/classify \
    -H "Content-Type: application/json" \
    -d '{"request": "The elevator is stuck on the third floor."}'
Response:

json
Copy code
{
    "priority": "High"
}
Technologies Used
Backend: Flask
Frontend: HTML, CSS
Machine Learning: Logistic Regression, Scikit-learn
Model Training: Python, Pandas, Scikit-learn
Deployment Ready: Easily adaptable for cloud services like AWS, Azure, or Heroku
Contributing
Contributions are welcome!

Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit your changes: git commit -m 'Add feature-name'.
Push to the branch: git push origin feature-name.
Open a pull request.