# Maintenance Priority Classifier

A Flask-based web application and REST API that classifies maintenance requests into priority levels using a pre-trained machine learning model.

---

## Features

- **Frontend**: A user-friendly interface for submitting maintenance requests.
- **REST API**: Programmatic access to classify maintenance requests.
- **Machine Learning Model**: Predicts the priority of maintenance tasks based on the request description.
- **Real-time Classification**: Quickly processes requests and returns priority labels like *High*, *Medium*, or *Low*.

---

## Demo

### Frontend

A simple interface where users can input maintenance issues and view their priority.

### REST API

**Endpoint**: `/api/classify`

- **Request** (JSON):

    ```json
    {
        "request": "The AC is leaking water."
    }
    ```

- **Response** (JSON):

    ```json
    {
        "priority": "High"
    }
    ```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/maintenance_priority_app.git
cd maintenance_priority_app
```


### 2. Clone the Repository
```bash
python3 -m venv venv
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Model (Optional)

#If you want to retrain the model, run the following:
```bash
python3 scripts/train_model.py
# This will generate the trained model and encoders in the app/models/ directory.
```


## Installation and Setup

### 1. Start the Flask Application
```bash
python3 app/app.py
```

### 2. Access the App
- **1. Frontend**: Open your browser and go to http://127.0.0.1:5000.
- **2. REST API**: Use a tool like Postman or curl to interact with the API.