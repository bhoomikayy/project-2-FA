from flask import Flask, render_template, request
import jsonify
import requests
import pickle
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('C:/Users/bhoom/Desktop/random_forest_regression_model.pkl', 'rb'))
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        team = int(request.form['team'])
        targeted_productivity = float(request.form['targeted_productivity'])
        smv=float(request.form['smv'])
        wip=float(request.form['wip'])
        over_time=int(request.form['over_time'])
        incentive= int(request.form['incentive'])
        idle_time= float(request.form['idle_time'])
        idle_men = int(request.form['idle_men'])
        no_of_style_change= int(request.form['no_of_style_change'])
        no_of_workers= float(request.form['no_of_workers'])


        quarter=request.form['quarter']
        if(quarter==1):
                quarter_Quarter1 = 1
                quarter_Quarter2 = 0
                quarter_Quarter3 = 0
                quarter_Quarter4 = 0
                quarter_Quarter5 = 0

        elif(quarter==2):
            quarter_Quarter1 = 0
            quarter_Quarter2 = 1
            quarter_Quarter3 = 0
            quarter_Quarter4 = 0
            quarter_Quarter5 = 0

        elif (quarter == 3):
            quarter_Quarter1 = 0
            quarter_Quarter2 = 0
            quarter_Quarter3 = 1
            quarter_Quarter4 = 0
            quarter_Quarter5 = 0

        elif (quarter == 4):
            quarter_Quarter1 = 0
            quarter_Quarter2 = 0
            quarter_Quarter3 = 0
            quarter_Quarter4 = 0
            quarter_Quarter5 = 0

        else:
            quarter_Quarter1 = 0
            quarter_Quarter2 = 0
            quarter_Quarter3 = 0
            quarter_Quarter4 = 0
            quarter_Quarter5 = 1


        department=request.form['department']
        if(department=='sewing'):
            department_sewing	= 1
            department_finishing= 0
        else:
            department_sewing = 0
            department_finishing = 1

        day=request.form['day']
        if (day== 'Monday'):
            day_Monday = 1
            day_Tuesday = 0
            day_Wednesday = 0
            day_Thursday = 0
            day_Friday = 0
            day_Saturday = 0
            day_Sunday = 0

        elif (day== 'Tuesday'):
            day_Monday = 0
            day_Tuesday = 1
            day_Wednesday = 0
            day_Thursday = 0
            day_Friday = 0
            day_Saturday = 0
            day_Sunday = 0

        elif (day== 'Wednesday'):
            day_Monday = 0
            day_Tuesday = 0
            day_Wednesday = 1
            day_Thursday = 0
            day_Friday = 0
            day_Saturday = 0
            day_Sunday = 0

        elif (day== 'Thursday'):
            day_Monday = 0
            day_Tuesday = 0
            day_Wednesday = 0
            day_Thursday = 1
            day_Friday = 0
            day_Saturday = 0
            day_Sunday = 0

        elif (day== 'Friday'):
            day_Monday = 0
            day_Tuesday = 0
            day_Wednesday = 0
            day_Thursday = 0
            day_Friday = 1
            day_Saturday = 0
            day_Sunday = 0

        elif (day== 'Saturday'):
            day_Monday = 0
            day_Tuesday = 0
            day_Wednesday = 0
            day_Thursday = 0
            day_Friday = 0
            day_Saturday = 1
            day_Sunday = 0

        else:
            day_Monday = 0
            day_Tuesday = 0
            day_Wednesday = 0
            day_Thursday = 0
            day_Friday = 0
            day_Saturday = 0
            day_Sunday = 1


        prediction=model.predict([[targeted_productivity,smv,wip,over_time,incentive,idle_time,no_of_style_change,no_of_workers,team, idle_men, quarter_Quarter1, quarter_Quarter2, quarter_Quarter3, quarter_Quarter4, quarter_Quarter5, department_sewing, department_finishing, day_Monday, day_Tuesday, day_Wednesday, day_Thursday, day_Friday, day_Saturday, day_Sunday]])
        output=round(prediction[0],2)
        if output> targeted_productivity:
            return render_template('index.html',prediction_texts="Great Productivity")
        else:
            return render_template('index.html',prediction_text="Poor Productivity")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)




