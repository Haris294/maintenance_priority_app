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
