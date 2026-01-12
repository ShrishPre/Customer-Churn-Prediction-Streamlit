# 📉 Customer Churn Prediction using Machine Learning

A complete **end-to-end Machine Learning project** that predicts whether a customer is likely to churn using the **Telco Customer Churn dataset**. The project includes data preprocessing, model training with **Gradient Boosting**, and deployment as an interactive **Streamlit web application**.

---

## 🚀 Live Demo

👉 *(Add your Streamlit app link here after deployment)*

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
git clone <your-repo-link>
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

---

## 🔮 Future Improvements

* Add SHAP / feature importance visualization
* Try advanced models (XGBoost, LightGBM)
* Improve UI with charts and metrics
* Add probability-based risk scoring

---

## 👩‍💻 Author

**Shrishti**
Aspiring Data Scientist | Machine Learning Enthusiast

🔗 GitHub: *(add your profile link)*
🔗 LinkedIn: *(add your LinkedIn link)*

---

⭐ If you like this project, feel free to **star the repository**!
