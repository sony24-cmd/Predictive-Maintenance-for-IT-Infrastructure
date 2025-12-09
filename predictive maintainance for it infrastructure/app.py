from flask import Flask, jsonify, render_template
import random, pickle, numpy as np
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Load ML model
model = pickle.load(open("models/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("layout.html")

@app.route("/anomaly")
def anomaly():
    return render_template("anomaly.html")

@app.route("/cloudplatform")
def cloudplatform():
    return render_template("cloudplatform.html")

@app.route("/data_analysis")
def data_analysis():
    return render_template("data_analysis.html")

@app.route("/visualization")
def visualization():
    return render_template("visualization.html")

# APIs ----------
@app.route("/api/anomaly_check")
def anomaly_check():
    value = random.randint(30, 100)
    return jsonify({
        "value": value,
        "is_anomaly": value > 85
    })

@app.route("/api/cloud_data")
def cloud_data():
    return jsonify({
        "instances": [
            {"name": "VM-01", "cpu": random.randint(20,90)},
            {"name": "VM-02", "cpu": random.randint(20,90)},
            {"name": "DB Server", "cpu": random.randint(20,90)}
        ],
        "storage": random.randint(40,95),
        "network": [random.randint(20,80) for _ in range(10)]
    })

@app.route("/api/sensor_logs")
def sensor_logs():
    logs = []
    for _ in range(25):
        logs.append({
            "time": f"{random.randint(1,12)}:{random.randint(10,59)}",
            "cpu": random.randint(20,95),
            "memory": random.randint(20,95),
            "disk": random.randint(20,95),
            "temp": random.randint(20,95),
            "network": random.randint(20,95)
        })
    return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True)
