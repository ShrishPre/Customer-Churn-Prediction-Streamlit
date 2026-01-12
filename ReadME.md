# 📉 Customer Churn Prediction using Machine Learning

A complete **end-to-end Machine Learning project** that predicts whether a customer is likely to churn using the **Telco Customer Churn dataset**. The project includes data preprocessing, model training with **Gradient Boosting**, and deployment as an interactive **Streamlit web application**.

---

## 🚀 Live Demo

👉 Local URL: http://localhost:8501
  Network URL: http://192.168.29.121:8501

---

## 📌 Problem Statement

Customer churn is a major challenge for subscription-based businesses. The goal of this project is to **predict whether a customer will leave the service (churn)** based on their demographic details, services subscribed, and billing information.

---

## 🧠 Solution Overview

* Cleaned and preprocessed real-world customer data
* Performed **exploratory data analysis (EDA)**
* Applied **one-hot encoding** for categorical features
* Trained a **Gradient Boosting Classifier**
* Handled feature consistency for deployment
* Built and deployed an interactive **Streamlit app**

---

## 🛠️ Tech Stack

* **Language:** Python 🐍
* **Libraries:**

  * pandas
  * numpy
  * scikit-learn
  * streamlit
* **Tools:**

  * Jupyter Notebook
  * VS Code
  * GitHub
  * Streamlit Cloud

---

## 📊 Machine Learning Model

* **Model Used:** Gradient Boosting Classifier
* **Type:** Supervised Learning (Classification)
* **Target Variable:** `Churn` (Yes / No)
* **Why Gradient Boosting?**

  * Handles non-linearity well
  * Strong performance on tabular data
  * Reduces bias and variance

---

## 🧩 Project Structure

```
customer-churn-project/
│
├── app.py                  # Streamlit application
├── model.pkl               # Trained model + feature names
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
│
├── notebooks/
│   └── customer_churn.ipynb
│
├── data/
│   └── Telco-Customer-Churn.csv
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone <(https://github.com/ShrishPre/Customer-Churn-Streamlit/tree/main)>
cd customer-churn-project
```

### 2️⃣ Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```bash
python -m streamlit run app.py
```

---

## 🖥️ Streamlit App Features

* User-friendly input form
* Real-time churn prediction
* Handles unseen categories safely
* Deployment-ready architecture

---

## 📈 Results

The model successfully predicts customer churn with strong performance on test data. Feature handling ensures reliable predictions even during deployment.
<img width="983" height="545" alt="image" src="https://github.com/user-attachments/assets/745b1fe5-4717-439c-b31e-a86c99adbae4" />

---

## 🔮 Future Improvements

* Add  feature importance visualization
* Try advanced models (XGBoost, LightGBM)
* Improve UI with charts and metrics
* Add probability-based risk scoring

---

## 👩‍💻 Author

**Shristi**
Aspiring Data Scientist | Machine Learning Enthusiast

🔗 GitHub: *(add your profile link)*
🔗 LinkedIn: *(add your LinkedIn link)*

---
<img width="1366" height="768" alt="Screenshot (372)" src="https://github.com/user-attachments/assets/32fdede2-b8c3-44ac-894a-796dee9b63a8" />

⭐ If you like this project, feel free to **star the repository**!
