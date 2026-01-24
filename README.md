# HealthCoverAI - Insurance Price Predictor 💰
This project predicts health insurance costs using a machine learning model. It uses Flask as a backend API and a clean HTML/CSS frontend for user interaction.
A web application for predicting health insurance costs using machine learning.

## Project Structure

```
project/
│
├── index.html              # Landing page
├── predictor.html          # Prediction form page
├── styles.css              # All styling
├── app.py                  # Flask backend server
├── requirements.txt        # Python dependencies
├── insurance_model.pkl     # Trained ML model 
└── README.md              # This file
```

## Setup Instructions

### Step 1: Install Python Dependencies

Open your terminal in PyCharm and run:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web server)
- Flask-CORS (for frontend-backend communication)
- pandas (data handling)
- joblib (model loading)
- scikit-learn (ML library). Model is trained using sickit learn 1.5.1 version.

### Step 2: Add Your Trained Model

**IMPORTANT:** Place your `insurance_model.pkl` file in the same directory as `app.py`

The model file should be the one you created with:
```python
joblib.dump(model, "insurance_model.pkl")
```

### Step 3: Start the Flask Backend

In your terminal, run:

```bash
python app.py
```

We should see:
```
🚀 Starting HealthCoverAI Backend Server...
📊 Model Status: Loaded ✅
🌐 Server running on http://localhost:5000
```

### Step 4: Open the Website

Open `index.html` in your web browser:
- **Option 1:** Double-click `index.html`
- **Option 2:** Right-click in PyCharm → "Open in Browser"
- **Option 3:** Go to `http://localhost:5000` in your browser

## 🎯 How It Works

1. **Landing Page (index.html):**
   - Beautiful hero section with features
   - Stats showing 88% accuracy and 24/7 availability
   - "Start Prediction" button to navigate to predictor

2. **Predictor Page (predictor.html):**
   - Form with all insurance parameters (age, sex, BMI, children, smoker, region)
   - Sends data to Flask backend when "Predict Price" is clicked
   - Displays real prediction from my trained ML model
   - Shows loading spinner while processing
   - Error handling if backend is not running

3. **Flask Backend (app.py):**
   - Loads your trained model on startup
   - Receives form data from frontend
   - Makes prediction using the model
   - Returns predicted insurance cost as JSON

## 🔧 API Endpoints

### `POST /predict`
Accepts JSON data and returns prediction:

**Request:**
```json
{
  "age": 25,
  "sex": "male",
  "bmi": 25.0,
  "children": 0,
  "smoker": "no",
  "region": "northeast"
}
```

**Response:**
```json
{
  "success": true,
  "predicted_cost": 3756.45
}
```

### `GET /health`
Health check endpoint:

**Response:**
```json
{
  "status": "running",
  "model_loaded": true
}
```

## ❗ Troubleshooting

### Issue: "Model not loaded" error
**Solution:** Make sure `insurance_model.pkl` is in the same folder as `app.py`

### Issue: "Cannot connect to server" error on website
**Solution:** Make sure Flask backend is running (`python app.py`)

### Issue: Port 5000 already in use
**Solution:** Either:
- Stop the other process using port 5000
- Change the port in `app.py`: `app.run(debug=True, port=5001)`
- Update the API URL in `predictor.html` to match

### Issue: CORS error in browser console
**Solution:** The flask-cors package should handle this. Make sure it's installed:
```bash
pip install flask-cors
```

## 🎨 Features

✨ **Beautiful UI**
- Modern gradient design
- Smooth animations
- Fully responsive (mobile-friendly)
- Medical-themed background

⚡ **Real-time Predictions**
- Loading spinner during prediction
- Instant results display
- Error handling

🔒 **Secure**
- Backend validation
- No data stored
- Local processing

## 📝 Notes

- The website connects to `http://localhost:5000` by default
- Make sure both Flask backend and frontend are running
- The model should accept the same features as your Streamlit app
- Form validation prevents invalid inputs

## 🤝 Support

If you encounter any issues:
1. Check that Flask is running
2. Verify `insurance_model.pkl` exists
3. Check browser console for errors (F12)
4. Check Flask terminal for errors

---

Made with ❤️ for better health coverage
