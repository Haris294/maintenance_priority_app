import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Step 1: Sample Data
data = pd.DataFrame({
    'request': [
        'Elevator is broken',
        'Leaking pipe',
        'Power outage',
        'Light bulb needs replacement',
        'Garbage not collected',
        'WiFi is down'
    ],
    'priority': ['High', 'High', 'Medium', 'Low', 'Low', 'Medium']
})

# Step 2: Vectorize Text Data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['request'])

# Step 3: Encode Priority Labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['priority'])

# Step 4: Train Logistic Regression Model
model = LogisticRegression()
model.fit(X, y)

# Step 5: Save Model and Encoders
joblib.dump(vectorizer, 'app/models/vectorizer.pkl')
joblib.dump(model, 'app/models/maintenance_model.pkl')
joblib.dump(label_encoder, 'app/models/label_encoder.pkl')

print("Model and encoders have been saved in the 'app/models/' folder.")
