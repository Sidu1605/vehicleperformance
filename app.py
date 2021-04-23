from flask import Flask, request, render_template
import requests
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('vehicleperformancemodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vehicleperformance' , methods=['GET','POST'])
def vehicleperformance():
    if request.method == "POST":

        # Name
        name = request.form['name']
        if (name == 'others'):
            name_others = 1
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'ford'):
            name_others = 0
            name_ford = 1
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'chevrolet'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 1
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'plymouth'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 1
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'dodge'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 1
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'amc'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'toyota'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 1
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'datsun'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 1
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'volkswagen'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 1
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'buick'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 1
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'pontiac'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 1
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'honda'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 1
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=0

        elif (name == 'mazda'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 1
            name_mercury = 0
            name_oldsmobile=0
        
        elif (name == 'mercury'):
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 1
            name_oldsmobile=0

        else:
            name_others = 0
            name_ford = 0
            name_chevrolet = 0
            name_plymouth = 0
            name_dodge = 0
            name_amc = 0
            name_toyota = 0
            name_datsun = 0
            name_volkswagen = 0
            name_buick = 0
            name_pontiac = 0
            name_honda = 0
            name_mazda = 0
            name_mercury = 0
            name_oldsmobile=1
        
        # Origin

        origin = int(request.form['origin'])
        if (origin == 1):
            origin_2 = 0
            origin_3 = 0
        elif (origin == 2):
            origin_2 = 1
            origin_3 = 0
        else :
            origin_2 = 0
            origin_3 = 1

        # year
        year = int(request.form['year'])
        Vehicle_Age = 2021 - year

        # Displacement
        displacement = int(request.form['displacement'])

        # Weight
        weight = int(request.form['weight'])

        # Horsepower
        horsepower = int(request.form['horsepower'])

        # Acceleration
        acceleration = int(request.form['acceleration'])

        # Cylinders
        cylinders = int(request.form['cylinders'])
        if (cylinders == 3):
            cylinders_4 = 0
            cylinders_5 = 0
            cylinders_6 = 0
            cylinders_8 = 0
        
        elif (cylinders == 4):
            cylinders_4 = 1
            cylinders_5 = 0
            cylinders_6 = 0
            cylinders_8 = 0
        
        elif (cylinders == 5):
            cylinders_4 = 0
            cylinders_5 = 0
            cylinders_6 = 1
            cylinders_8 = 0
        
        elif (cylinders == 6):
            cylinders_4 = 0
            cylinders_5 = 0
            cylinders_6 = 1
            cylinders_8 = 0
        
        else:
            cylinders_4 = 0
            cylinders_5 = 0
            cylinders_6 = 0
            cylinders_8 = 1
        
        prediction = model.predict([[displacement,horsepower, weight, acceleration,Vehicle_Age, origin_2, origin_3, cylinders_4, cylinders_5,
                             cylinders_6, cylinders_8, name_buick, name_chevrolet,
                             name_datsun, name_dodge, name_ford, name_honda, name_mazda,
                             name_mercury, name_oldsmobile, name_others, name_plymouth,
                             name_pontiac, name_toyota, name_volkswagen]])

        output=round(prediction[0],2)

        return render_template('VP form.html',prediction_text="The Mileage Of Your Car Is  {} Km/l".format(output))

    return render_template('VP form.html')






if __name__ == "__main__":
    app.run(debug=True)




