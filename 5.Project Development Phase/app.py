from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model/trained_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    rainfall = float(request.form["rainfall"])
    waterlevel = float(request.form["waterlevel"])
    humidity = float(request.form["humidity"])

    prediction = model.predict([[rainfall, waterlevel, humidity]])

    if prediction[0] == 1:
        result = "Flood Likely"
    else:
        result = "No Flood"

    return render_template("result.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)