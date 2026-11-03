import json
import joblib
import numpy as np

from pathlib import Path
from http.server import BaseHTTPRequestHandler
from sklearn.datasets import load_iris

# Load the trained machine learning model
MODEL_PATH = Path(__file__).resolve().parent.parent / "iris_model.pkl"

model = joblib.load(MODEL_PATH)

# Load flower species names
iris = load_iris()
flower_names = iris.target_names


class handler(BaseHTTPRequestHandler):

    def do_POST(self):

        try:
            # Read the data sent by the website
            content_length = int(self.headers.get("Content-Length", 0))
            request_data = self.rfile.read(content_length)

            data = json.loads(request_data)

            # Get the four flower measurements
            measurements = [
                float(data["sepal_length"]),
                float(data["sepal_width"]),
                float(data["petal_length"]),
                float(data["petal_width"])
            ]

            # Prepare input for the machine learning model
            input_data = np.array([measurements])

            # Make prediction
            prediction = model.predict(input_data)[0]
            probabilities = model.predict_proba(input_data)[0]

            predicted_species = flower_names[int(prediction)]
            confidence = float(probabilities[int(prediction)] * 100)

            # Prepare the response
            response = {
                "predicted_species": predicted_species,
                "confidence": round(confidence, 2),
                "probabilities": {
                    flower_names[i]: round(float(probabilities[i] * 100), 2)
                    for i in range(len(flower_names))
                }
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(json.dumps(response).encode())

        except Exception as error:

            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            response = {"error": str(error)}

            self.wfile.write(json.dumps(response).encode())