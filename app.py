from flask import Flask, request, render_template
import joblib
import pandas as pd
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the scaler and K-Means model
scaler = joblib.load('scaler.pkl')
kmeans = joblib.load('kmeans_model.pkl')

# Define cluster-to-segment mapping (adjust based on your cluster analysis)
cluster_to_segment = {
    0: "Young budget customers",
    1: "High earners who spend less",
    2: "Premium customers",
    3: "Middle-class spenders",
    4: "Budget-conscious spenders"
}

# Route for the homepage (form)
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        income = float(request.form['income'])
        spending_score = float(request.form['spending_score'])

        # Validate inputs
        if income < 0 or spending_score < 0 or spending_score > 100:
            return render_template('index.html', error="Invalid input. Income and Spending Score must be non-negative, and Spending Score must be <= 100.")

        # Create DataFrame for input
        input_data = pd.DataFrame([[income, spending_score]], 
                                 columns=['Annual Income (k$)', 'Spending Score (1-100)'])

        # Scale the input
        input_scaled = scaler.transform(input_data)

        # Predict the cluster
        cluster = kmeans.predict(input_scaled)[0]

        # Get the customer segment
        segment = cluster_to_segment[cluster]

        # Return result to the template
        return render_template('index.html', 
                             cluster=cluster, 
                             segment=segment, 
                             income=income, 
                             spending_score=spending_score)
    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)