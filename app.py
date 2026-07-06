from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load Model and Scaler
model = pickle.load(open("rdf.pkl", "rb"))
scaler = pickle.load(open("scale1.pkl", "rb"))


# -----------------------------
# Home Page
# -----------------------------
@app.route('/')
def home():
    return render_template("home.html")

# -----------------------------
# About Page
# -----------------------------
@app.route('/about')
def about():
    return render_template("about.html")

# -----------------------------
# Workflow Page
# -----------------------------
@app.route('/workflow')
def workflow():
    return render_template("workflow.html")


# -----------------------------
# Performance Page
# -----------------------------
@app.route('/performance')
def performance():
    return render_template("performance.html")


# -----------------------------
# Tips Page
# -----------------------------
@app.route('/tips')
def tips():
    return render_template("tips.html")


# -----------------------------
# Contact Page
# -----------------------------
@app.route('/contact')
def contact():
    return render_template("contact.html")


# -----------------------------
# Prediction Form
# -----------------------------
@app.route('/predict')
def predict():
    return render_template("predict.html")


# -----------------------------
# Prediction Result
# -----------------------------
@app.route('/submit', methods=['POST'])
def submit():

    try:

        Gender = float(request.form['Gender'])
        Married = float(request.form['Married'])
        Dependents = float(request.form['Dependents'])
        Education = float(request.form['Education'])
        Self_Employed = float(request.form['Self_Employed'])
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        Credit_History = float(request.form['Credit_History'])
        Property_Area = float(request.form['Property_Area'])

        values = np.array([[

            Gender,
            Married,
            Dependents,
            Education,
            Self_Employed,
            ApplicantIncome,
            CoapplicantIncome,
            LoanAmount,
            Loan_Amount_Term,
            Credit_History,
            Property_Area

        ]])

        values = scaler.transform(values)

        prediction = model.predict(values)[0]

        return render_template(
            "submit.html",
            prediction=prediction
        )

    except Exception as e:

        return f"Error : {e}"


# -----------------------------
# Main
# -----------------------------
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
