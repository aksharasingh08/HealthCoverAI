from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# =========================
# Load the trained model
# =========================
try:
    model = joblib.load("insurance_model.pkl")
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None


# =========================
# Page routes (HTML)
# =========================
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET"])
def predictor_page():
    return render_template("predictor.html")


# =========================
# API route (POST prediction)
# =========================
@app.route("/predict", methods=["POST"])
def predict_api():
    try:
        data = request.get_json()

        if model is None:
            return jsonify({
                "success": False,
                "error": "Model not loaded. Please check insurance_model.pkl"
            }), 500

        # Convert input to DataFrame
        input_data = pd.DataFrame({
            "age": [int(data["age"])],
            "sex": [data["sex"]],
            "bmi": [float(data["bmi"])],
            "children": [int(data["children"])],
            "smoker": [data["smoker"]],
            "region": [data["region"]]
        })

        # Predict
        prediction = model.predict(input_data)
        predicted_cost = float(prediction[0])

        return jsonify({
            "success": True,
            "predicted_cost": round(predicted_cost, 2)
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400


# =========================
# Health check
# =========================
@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "model_loaded": model is not None
    })


# =========================
# Run app
# =========================
import os

if __name__ == "__main__":
    print("🚀 Starting HealthCoverAI Backend Server...")
    print("📊 Model Status:", "Loaded ✅" if model else "Not Found ❌")
    app.run(host="0.0.0.0", port=5000)



