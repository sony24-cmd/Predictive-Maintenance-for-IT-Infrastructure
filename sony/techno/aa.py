from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Prediction model
class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpu_usage = db.Column(db.Float, nullable=False)
    memory_usage = db.Column(db.Float, nullable=False)
    disk_usage = db.Column(db.Float, nullable=False)
    network_usage = db.Column(db.Float, nullable=False)
    predicted_capacity = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Prediction {self.id}>"

# Create the database and tables
with app.app_context():
    db.create_all()

# Load the trained model
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

# Route to serve the frontend
@app.route('/')
def home():
    return render_template('index.html')  # Serve the index.html template

# Route to handle prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.get_json()
        cpu_usage = data['cpu_usage']
        memory_usage = data['memory_usage']
        disk_usage = data['disk_usage']
        network_usage = data['network_usage']

        # Prepare input for the model
        input_data = np.array([[cpu_usage, memory_usage, disk_usage, network_usage]])

        # Make prediction
        predicted_capacity = model.predict(input_data)[0]

        # Save the prediction to the database
        prediction = Prediction(
            cpu_usage=cpu_usage,
            memory_usage=memory_usage,
            disk_usage=disk_usage,
            network_usage=network_usage,
            predicted_capacity=predicted_capacity
        )
        db.session.add(prediction)
        db.session.commit()

        # Return the result
        return jsonify({
            'predicted_capacity': predicted_capacity
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

# Route to view all predictions
@app.route('/predictions', methods=['GET'])
def get_predictions():
    try:
        # Fetch all predictions from the database
        predictions = Prediction.query.all()
        predictions_list = []
        for prediction in predictions:
            predictions_list.append({
                'id': prediction.id,
                'cpu_usage': prediction.cpu_usage,
                'memory_usage': prediction.memory_usage,
                'disk_usage': prediction.disk_usage,
                'network_usage': prediction.network_usage,
                'predicted_capacity': prediction.predicted_capacity
            })
        return jsonify(predictions_list)
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)