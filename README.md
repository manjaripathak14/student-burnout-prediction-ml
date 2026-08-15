# Student Burnout Prediction 

A Machine Learning based web application that predicts the overall impact of social media and lifestyle factors on students as **Negative, Neutral, or Positive**.

The project combines Machine Learning with a Flask-based web interface, allowing users to enter their personal and lifestyle-related information and receive a predicted overall impact.

---

##  Problem Statement

Students' social media usage, sleep patterns, mental health, and academic performance can affect their overall well-being.

The aim of this project is to use Machine Learning to identify the possible overall impact on a student based on factors such as social media usage, sleep, mental health score, academic level, and other related information.

---

##  Dataset

The dataset contains **1,705 student records** and 11 columns.

### Features

- Age
- Gender
- Academic Level
- Country
- Average Daily Social Media Usage Hours
- Most Used Social Media Platform
- Whether Social Media Affects Academic Performance
- Sleep Hours Per Night
- Mental Health Score

### Target Variable

**Overall Impact**

- Negative
- Neutral
- Positive

---

##  Data Preprocessing

The following preprocessing steps were performed:

- Removed `Student_ID` because it does not contribute to prediction.
- Used **Label Encoding** for the target variable.
- Used **One-Hot Encoding** for categorical features.
- Split the dataset into training and testing sets using an **80:20 ratio**.
- The final dataset contained **129 features** for prediction.

---

##  Machine Learning Models

Three Machine Learning classification models were implemented:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

##  Model Performance

The Random Forest model achieved an accuracy of approximately **99.12%** on the test dataset.

| Model | Accuracy |
|------|----------|
| Logistic Regression | Evaluated |
| Decision Tree | Evaluated |
| Random Forest | **99.12%** |

Random Forest was used as the main prediction model because of its strong performance on the dataset.

The Random Forest classification report also showed approximately **0.99 weighted average precision, recall, and F1-score**.

---

##  Feature Importance

Feature importance was analyzed using the Random Forest model to understand which factors contributed most to the predictions.

The project also includes a visualization of the **Top 10 Most Important Features**.

This helps make the model more interpretable instead of treating it as a complete black box.

---

##  Web Application

A Flask-based web application was developed to make the Machine Learning model interactive.

Users can enter:

- Age
- Gender
- Academic Level
- Country
- Average Daily Social Media Usage
- Most Used Social Media Platform
- Effect of Social Media on Academic Performance
- Sleep Hours
- Mental Health Score

The entered information is converted into the same format used during model training and passed to the trained Machine Learning model.

The application then predicts the student's **Overall Impact** as:

**Negative / Neutral / Positive**

---

##  Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Seaborn**
- **Flask**
- **HTML**
- **CSS**

---

##  Project Structure

```text
student-burnout-prediction-ml/
│
├── app.py
├── model.py
├── studentBurnOut.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
