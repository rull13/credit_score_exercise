from flask import Flask, jsonify, json, request, render_template
from logging import debug
app = Flask(__name__)
import pickle
from predict import predict_data

users = []


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template("index.html")



@app.route("/pred", methods=['POST','GET'])
def make_predictions():
    if request.method == 'POST':
        data = request.get_json()
        # print(data)
        result = predict_data(data)
        result = {
            'model':'german-credit-risk',
            "version": '1.0.0',
            "score_proba":result[0]

        }
        print(result)
        return jsonify(result)

@app.route('/result', methods=['POST','GET'])
def result_pred():

    data = {}

    data["Age"] = request.form.get("Age")
    data["Sex"] = request.form.get("Sex")
    data["Job"] = request.form.get("Job")
    data["Housing"] = request.form.get("Housing")
    data["Saving accounts"] = request.form.get("saving_account")
    data["Checking account"] = request.form.get("checking_account")
    data["Credit amount"] = request.form.get("credit_amount")
    data["Duration"] = request.form.get("duration")
    data["Purpose"] = request.form.get("purpose")
    result = predict_data(data)
    hasil = {
        'model':'german-credit-risk',
        "version": '1.0.0',
        "score_proba":result[0]

    }
    print(hasil)
    prediction = str(round(list(result)[0], 3))
    return render_template('result.html', name=prediction)

if __name__ == '__main__':
    app.run(port=3000, debug=False)
