import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("studentBurnOut.csv")


# ==========================
# Remove Student ID
# ==========================

df = df.drop("Student_ID", axis=1)


# ==========================
# Encode Target
# ==========================

le = LabelEncoder()

df["Overall_Impact"] = le.fit_transform(
    df["Overall_Impact"]
)


# ==========================
# One Hot Encoding
# ==========================

df = pd.get_dummies(
    df,
    columns=[
        "Gender",
        "Academic_Level",
        "Country",
        "Most_Used_Platform",
        "Affects_Academic_Performance"
    ],
    drop_first=True
)


# ==========================
# Features and Target
# ==========================

X = df.drop("Overall_Impact", axis=1)

y = df["Overall_Impact"]


# ==========================
# Train Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================
# Decision Tree
# ==========================

tree_model = DecisionTreeClassifier(
    random_state=42
)

tree_model.fit(X_train, y_train)


# ==========================
# Logistic Regression
# ==========================

log_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

log_model.fit(X_train, y_train)


# ==========================
# Random Forest
# ==========================

model = RandomForestClassifier(
    random_state=42
)

model.fit(X_train, y_train)


# ==========================
# Prediction Function
# ==========================

def predict_student(
    age,
    gender,
    academic_level,
    country,
    usage,
    platform,
    academic,
    sleep,
    mental
):

    # Create empty row with exactly
    # the same columns as X

    user_data = pd.DataFrame(
        np.zeros(
            (1, len(X.columns))
        ),
        columns=X.columns
    )


    # ==========================
    # Numeric Features
    # ==========================

    user_data["Age"] = age

    user_data["Avg_Daily_Usage_Hours"] = usage

    user_data["Sleep_Hours_Per_Night"] = sleep

    user_data["Mental_Health_Score"] = mental


    # ==========================
    # Gender
    # ==========================

    if gender == "Male":

        if "Gender_Male" in user_data.columns:
            user_data["Gender_Male"] = 1


    # ==========================
    # Academic Level
    # ==========================

    if academic_level == "High School":

        column = "Academic_Level_High School"

        if column in user_data.columns:
            user_data[column] = 1


    elif academic_level == "Undergraduate":

        column = "Academic_Level_Undergraduate"

        if column in user_data.columns:
            user_data[column] = 1


    # Graduate is the dropped category
    # because we used drop_first=True


    # ==========================
    # Academic Performance
    # ==========================

    if academic == "Yes":

        column = "Affects_Academic_Performance_Yes"

        if column in user_data.columns:
            user_data[column] = 1


    # ==========================
    # Country
    # ==========================

    country_column = "Country_" + country

    if country_column in user_data.columns:

        user_data[country_column] = 1


    # ==========================
    # Platform
    # ==========================

    platform_column = (
        "Most_Used_Platform_" + platform
    )

    if platform_column in user_data.columns:

        user_data[platform_column] = 1


    # ==========================
    # Predictions
    # ==========================

    rf_prediction = model.predict(user_data)

    tree_prediction = tree_model.predict(user_data)

    log_prediction = log_model.predict(user_data)


    # Convert numbers back to labels

    rf_result = le.inverse_transform(
        rf_prediction
    )[0]

    tree_result = le.inverse_transform(
        tree_prediction
    )[0]

    log_result = le.inverse_transform(
        log_prediction
    )[0]


    return {
        "Random Forest": rf_result,
        "Decision Tree": tree_result,
        "Logistic Regression": log_result
    }