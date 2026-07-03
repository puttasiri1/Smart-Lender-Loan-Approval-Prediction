# Smart Lender - AI Loan Approval Prediction System

## 📌 Project Overview

Smart Lender is a Machine Learning-based web application that predicts whether a loan application is likely to be approved based on applicant details. The system helps financial institutions make faster and more accurate lending decisions.

---

## 🚀 Features

- AI-based Loan Approval Prediction
- User-friendly Web Interface
- Real-time Prediction using Flask
- Random Forest Machine Learning Model
- Responsive and Modern UI
- Fast and Accurate Decision Support

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Imbalanced-learn (SMOTE)
- Pickle

---

## 📂 Project Structure

```
Smart-Lender
│
├── Dataset
│   └── loan_prediction.csv
│
├── Training
│   └── Loan Prediction using ML.ipynb
│
├── Flask
│   ├── app.py
│   ├── rdf.pkl
│   ├── scale1.pkl
│   ├── templates
│   │   ├── home.html
│   │   ├── predict.html
│   │   └── submit.html
│   └── static
│       └── css
│           └── style.css
│
├── README.md
└── requirements.txt
```

---

## 📊 Machine Learning Models

The following algorithms were trained and evaluated:

- Decision Tree
- K-Nearest Neighbors (KNN)
- Gradient Boosting
- Random Forest (Best Performing Model)

The Random Forest model is deployed in the Flask application.

---

## ▶️ How to Run the Project

### Step 1

Clone the repository

```bash
git clone https://github.com/YourUsername/Smart-Lender-Loan-Approval-Prediction.git
```

### Step 2

Navigate to the Flask folder

```bash
cd Flask
```

### Step 3

Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4

Run the application

```bash
python app.py
```

### Step 5

Open your browser

```
http://127.0.0.1:5000
```

---

## 📈 Input Parameters

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

---

## 🎯 Output

The system predicts:

- ✅ Loan Approved
- ❌ Loan Not Approved

---

## 👩‍💻 Developed By

**Siri Putta**

SmartBridge AI & ML Project

2026