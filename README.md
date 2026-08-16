# Student Burnout Prediction

A Machine Learning based web application that predicts the overall impact of social media and lifestyle factors on students as **Negative, Neutral, or Positive**.

The project combines Machine Learning with a Flask-based web interface, allowing users to enter their personal and lifestyle-related information and receive a predicted overall impact.

---

## Problem Statement

Students' social media usage, sleep patterns, mental health, and academic performance can affect their overall well-being.

The aim of this project is to use Machine Learning to identify the possible overall impact on a student based on factors such as social media usage, sleep, mental health score, academic level, and other related information.

---
## 🌐 Live Demo

Try the deployed web application here:

👉 https://student-burnout-prediction-ml-1.onrender.com/

## Dataset

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

## Data Preprocessing

The following preprocessing steps were performed:

- Removed `Student_ID` because it does not contribute to prediction.
- Used **Label Encoding** for the target variable.
- Used **One-Hot Encoding** for categorical features.
- Split the dataset into training and testing sets using an **80:20 ratio**.
- The final dataset contained **129 features** for prediction.

---

## Machine Learning Models

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

## Model Performance

The Random Forest model achieved an accuracy of approximately **99.12%** on the test dataset.

| Model | Accuracy |
|---|---:|
| Logistic Regression | Evaluated |
| Decision Tree | Evaluated |
| Random Forest | **99.12%** |

Random Forest was used as the main prediction model because of its strong performance on the dataset.

The Random Forest classification report also showed approximately **0.99 weighted average precision, recall, and F1-score**.

---

## Feature Importance

Feature importance was analyzed using the Random Forest model to understand which factors contributed most to the predictions.

The project also includes a visualization of the **Top 10 Most Important Features**.

This helps make the model more interpretable instead of treating it as a complete black box.

---

## Web Application

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

## Technologies Used

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

## Project Structure

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
```

---

##  How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/manjaripathak14/student-burnout-prediction-ml.git
```

### 2. Open the Project Folder

```bash
cd student-burnout-prediction-ml
```

### 3. Install the Required Libraries

```bash
pip install pandas numpy scikit-learn matplotlib seaborn flask
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open the Web Application

After running the application, open the URL shown in the terminal:

```text
http://127.0.0.1:5000
```

### 6. Use the Application

1. Enter the required student information.
2. Submit the form.
3. The trained Machine Learning model processes the input.
4. The predicted **Overall Impact** is displayed on the result page.

---

##  Future Improvements

This project can be further improved and extended in the following ways:

### AI Integration

An AI-based conversational assistant can be added to the application to explain the prediction in simple language and provide personalized, general well-being suggestions based on the user's inputs.

### Online Deployment

The Flask application can be deployed online so that users can access the prediction system directly through a web browser without running the project locally.

### More Machine Learning Models

Additional models such as **XGBoost, LightGBM, and CatBoost** can be implemented and compared with the existing models to explore whether prediction performance can be improved.

### Additional Features

More student-related factors such as study hours, academic workload, physical activity, and other lifestyle factors can be included to make the prediction more comprehensive.

### Explainable AI

Techniques such as **SHAP** or **LIME** can be added to explain why the model produced a particular prediction and which features influenced the result.

### Larger and More Diverse Dataset

Using a larger and more diverse dataset can help improve the model's ability to generalize to different groups of students.

### Improved User Experience

The web interface can be further improved with responsive design, better visualizations, interactive charts, and a more personalized user experience.

---

##  Disclaimer

This project is developed for **educational and demonstration purposes only**.

The prediction generated by the application should not be considered a medical or psychological diagnosis. Mental health is complex and cannot be determined accurately using only a limited number of inputs.

---

##  Author

**Manjari Pathak**

B.Tech CSE-AI  
Indira Gandhi Delhi Technical University for Women (IGDTUW)

---

⭐ If you find this project interesting, feel free to explore the repository!
