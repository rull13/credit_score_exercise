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
            'model':'credit_risk_exercise',
            "version": '1.0.0',
            "score_proba":str(result)

        }
        print(result)
        return jsonify(result)

@app.route('/result', methods=['POST','GET'])
def result_pred():

    data = {}

    data["person_home_ownership"] = request.form.get("Home_Ownership")
    data["loan_intent"] = request.form.get("loan_intent")
    data["loan_grade"] = request.form.get("loan_grade")
    data["cb_person_default_on_file"] = request.form.get("Historical_default")
    data["person_age"] = request.form.get("Age")
    data["person_income"] = request.form.get("Annual_Income")
    data["person_emp_length"] = request.form.get("EmploymentLength")
    data["loan_int_rate"] = request.form.get("Interest_rate")
    data["loan_percent_income"] = request.form.get("PercentIncome")
    data["cb_person_cred_hist_length"] = request.form.get("CreditHistoryLength")
    data["loan_amnt"] = request.form.get("LoanAmount")
    print(data)
    result = predict_data(data)
    hasil = {
        'model':'credit_risk_exercise',
        "version": '1.0.0',
        "score_proba":str(result)

    }
    print(hasil)
    prediction = str(result)
    return render_template('result.html', name=prediction)

if __name__ == '__main__':
    app.run(port=3000, debug=False)
