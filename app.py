from flask import*
from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route("/", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        oxygen = request.form.get("oxygen")
        temperature = request.form.get("temperature")
        humidity = request.form.get("humidity")
        result = [oxygen, temperature, humidity]

        inp = np.array([int(i) for i in result])
        prediction = model.predict_proba([inp])
        output = '{0:.{1}f}'.format(prediction[0][1], 2)
        # if output > str(0.5):
        #     return render_template('firepred.html', pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output))
        # else:
        #     return render_template('firepred.html', pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output))
        # return "get"+" "+output
        res = result
        res.append(output)

        return render_template("success.html", result=res)

        # return result[0]
    return render_template("firepred.html")
# @app.route('/',)
# def predict():


if __name__ == '__main__':
    app.run(debug=True)
