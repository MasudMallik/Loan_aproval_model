# 🏦 Loan Approval Prediction System

A full-stack Machine Learning application that predicts whether a loan should be approved based on user details. This project combines Machine Learning, MLOps, authentication, and modern web technologies into a production-ready system.

---

## 🚀 Features

* 🔍 Loan approval prediction using ML model
* 🤖 Multiple models trained & compared:

  * Logistic Regression
  * Decision Tree Classifier
  * Random Forest Classifier
  * Support Vector Classifier (SVC)
  * ✅ XGBoost Classifier (Selected Best Model)
* 📊 Experiment tracking with MLflow (DagsHub)
* 📦 Data versioning with DVC
* 🔐 Secure authentication system:

  * Password hashing using bcrypt
  * Token-based authentication using PyJWT
* 📧 Email OTP verification using aiosmtplib
* ⚡ OTP storage using Redis (in-memory database)
* 🗄️ MongoDB Atlas for storing:

  * User details
  * Prediction/search history
* ⚡ Backend built with FastAPI + Pydantic
* 🎨 Frontend built with Streamlit
* 🐳 Fully containerized using Docker

---

## 🧠 Machine Learning Workflow

1. Data preprocessing
2. Feature engineering
3. Model training with multiple algorithms
4. Experiment tracking using MLflow (DagsHub)
5. Model comparison
6. Best model selection (XGBoost)
7. Model export using joblib

---

## 📁 Project Structure

```
.
├── backend/
│   ├── dockerfile                # Backend Docker configuration
│   ├── dvc.yaml                  # DVC pipeline configuration
│   ├── dvc.lock                  # DVC lock file
│   ├── preprocess.joblib         # Preprocessing pipeline
│   ├── preprocess.joblib.dvc     # DVC tracked file
│   ├── loan_predict.joblib       # Final trained model (XGBoost)
│   ├── model_train.py            # Model training script
│   ├── main.py                   # FastAPI entry point
│   ├── logger.py                 # Logging utility
│   ├── mlflow.db                 # MLflow tracking DB
│   ├── requirements.txt          # Backend dependencies
│   ├── *.ipynb                   # Experiment notebooks
│
├── frontend/
│   ├── dockerfile                # Frontend Docker configuration
│   ├── main.py                   # Streamlit app entry
│   ├── requirements.txt          # Frontend dependencies
│   ├── pages/
│   │   ├── home_page.py          # Home page UI
│   │   ├── login_reg.py          # Login & Registration
│   │   ├── predict.py            # Prediction UI
│   │   ├── history.py            # User history page
├── setup.py                      # Create project files
├── README.md                     # Project documentation
└── LICENSE
```

---

## ⚙️ Tech Stack

| Layer            | Technology            |
| ---------------- | --------------------- |
| Machine Learning | Scikit-learn, XGBoost |
| Backend          | FastAPI, Pydantic     |
| Frontend         | Streamlit             |
| Database         | MongoDB Atlas         |
| Cache/OTP        | Redis                 |
| Auth             | PyJWT, bcrypt         |
| Email            | aiosmtplib            |
| MLOps            | MLflow (DagsHub), DVC |
| DevOps           | Docker                |

---

## 🐳 Docker Setup

### Pull Docker Image

```
docker pull masud00/loan_predict_frontend:latest
docker pull masud00/loan_predict_backend:latest
```

### Run Container

```
docker run loan_predict_frontend:latest
docker run loan_predict_frontend:latest
```

---

## ▶️ Run Locally

### 1. Clone Repository

```
git clone https://github.com/MasudMallik/Loan_aproval_model.git

```

### 2. Backend Setup

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Frontend Setup

```
cd frontend
pip install -r requirements.txt
streamlit run main.py
```

---

## 🔐 Authentication Flow

1. User registers with email
2. OTP sent via email (aiosmtplib)
3. OTP stored temporarily in Redis
4. Password securely hashed using bcrypt
5. JWT token generated using PyJWT

---

## 📊 Input Features

* person_age
* person_gender
* person_education
* person_income
* person_home_ownership
* loan_amnt
* loan_intent
* loan_int_rate
* cb_person_cred_hist_length
* credit_score
* previous_loan_defaults_on_file

---

## 📈 Future Improvements

* Add model explainability (SHAP)
* Deploy using Kubernetes
* Add monitoring & logging dashboards
* Improve UI/UX

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Masud Mallik
