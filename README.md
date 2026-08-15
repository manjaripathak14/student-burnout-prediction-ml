\# Student Burnout Prediction 

A machine learning project that predicts the overall impact of social media and lifestyle factors on students as **Negative, Neutral, or Positive**.

##  Problem Statement

Students' social media usage, sleep patterns, mental health, and academic performance can have an impact on their overall well-being.

The aim of this project is to use machine learning to predict the **Overall Impact** based on different student-related factors.

##  Dataset

The dataset contains **1,705 student records** with 11 columns.

### Features used:
- Age
- Gender
- Academic Level
- Country
- Average Daily Usage Hours
- Most Used Social Media Platform
- Whether social media affects academic performance
- Sleep Hours Per Night
- Mental Health Score

### Target:
- Overall Impact → Negative / Neutral / Positive

##  Data Preprocessing

The dataset was processed using:

- Removed `Student_ID` as it is not useful for prediction.
- Label Encoding for the target variable.
- One-Hot Encoding for categorical features.
- Train-test split with 80% training data and 20% testing data.

##  Machine Learning Models

Three classification models were implemented and compared:

- Logistic Regression
- Decision Tree
- Random Forest

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

##  Random Forest Performance

The Random Forest model achieved approximately **99.12% accuracy** on the test set.

The confusion matrix and feature importance were also used to understand the model's performance and the factors contributing to predictions.

##  Web Application

A Flask-based web interface was created for the project.

Users can enter:

- Age
- Gender
- Academic Level
- Country
- Daily Social Media Usage
- Most Used Platform
- Academic Performance Impact
- Sleep Hours
- Mental Health Score

The trained machine learning model then predicts the student's **Overall Impact**.

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Flask
- HTML
- CSS

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
