from flask import Flask, render_template, request

from model import predict_student


app = Flask(__name__)


# ==========================
# Home Page
# ==========================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================
# Prediction
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])

    gender = request.form["gender"]

    academic_level = request.form["academic_level"]

    country = request.form["country"].strip().title()

    usage = float(
        request.form["social_media_usage"]
    )

    platform = request.form["platform"]

    academic = request.form["social_media_effect"]

    sleep = float(
        request.form["sleep_hours"]
    )

    mental = float(
        request.form["mental"]
    )


    # ==========================
    # Platform Name Formatting
    # ==========================

    platform_map = {

        "Whatsapp": "WhatsApp",

        "Youtube": "YouTube",

        "Linkedin": "LinkedIn",

        "Tiktok": "TikTok",

        "Wechat": "WeChat",

        "Vkontakte": "VKontakte",

        "Line": "LINE"

    }

    platform = platform_map.get(
        platform,
        platform
    )


    # ==========================
    # Get Predictions
    # ==========================

    predictions = predict_student(

        age,

        gender,

        academic_level,

        country,

        usage,

        platform,

        academic,

        sleep,

        mental

    )


    # ==========================
    # Result Page
    # ==========================

    return render_template(

        "result.html",

        predictions=predictions

    )


if __name__ == "__main__":

    app.run(debug=True)