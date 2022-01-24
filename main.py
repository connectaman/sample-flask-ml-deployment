from flask import Flask, render_template, request
from predict import predict_insurance
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        age = request.form['age']
        bmi = request.form['bmi']
        gender = request.form['gender']
        children = request.form['children']
        smoker = request.form['smoker']
        region = request.form['region']
        data = {
            "age":age,
            "gender":gender,
            "bmi":bmi,
            "children":children,
            "smoker":smoker,
            "region":region
        }
        res = predict_insurance(data)
        print(res)
        return render_template('index.html',insurance_price = round(res['result'][0],2))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="0.0.0.0")
