import boto3
import pickle
import pandas as pd
from flask import Flask, jsonify, request

# Set AWS access keys
access_key = ''
secret_key = ''

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Load the model from the S3 bucket
#s3 = boto3.client('s3')
s3.download_file('loan-model-bucket-897475', 'loan_model.pkl', '/tmp/model.pkl')
with open('/tmp/model.pkl', 'rb') as f:
    model = pickle.load(f)


# Initialize the Flask application
app = Flask(__name__)

# Define the endpoint to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Convert the input data to a DataFrame
    input_data = pd.DataFrame.from_dict(data)

    # Make predictions using the trained model
    predictions = model.predict(data)

    # Return the predictions as a JSON response
    return jsonify({'predictions': predictions.tolist()})

# Start the Flask application
if __name__ == '__main__':
    app.run()