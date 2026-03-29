# Heart Disease Prediction ❤️

This project predicts heart disease using Machine Learning and Deep Learning models.

## Models Used
- Logistic Regression
- Random Forest
- SVM
- ANN

## Accuracy
- Random Forest: 87.5%

## Features
- Streamlit Web App
- Real-time prediction
- User-friendly interface with comprehensive patient data input
- Supports 15 clinical features for accurate predictions

## Project Structure
```
heart_project/
├── app.py                 # Streamlit web application
├── model.pkl              # Trained Random Forest model
├── scaler.pkl             # StandardScaler for feature normalization
├── requirements.txt       # Python package dependencies
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd heart_project
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

## How to Run

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to:
```
http://localhost:8503
```

3. Enter patient details:
   - Age
   - Resting Blood Pressure
   - Cholesterol
   - Fasting Blood Sugar
   - Max Heart Rate
   - Oldpeak (ST depression)
   - Sex
   - Chest Pain Type
   - Resting ECG
   - Exercise Angina
   - ST Slope

4. Click "Predict" to get the result

## Requirements
- Python 3.7+
- streamlit
- numpy
- scikit-learn
- pandas

## Expected Output
The app will display:
- ✅ Low risk of Heart Disease (Green)
- ⚠️ High risk of Heart Disease (Red)

## Author
Your Name

## License
MIT License
