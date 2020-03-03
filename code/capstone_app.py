import numpy as np
import pandas as pd
import pickle
import re
from flask import Flask, request, Response, render_template

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

i = -1

app = Flask('Capstone')

@app.route('/form')

def form():
    return render_template('form1.html')

@app.route('/submit')

def submit():
    global i
    i += 1
    print(i)
    testinc = pd.read_csv('../data/testinc.csv')
    
    user_input = request.args
    #print(*user_input, sep='\n')
    
    if i == 0:
        global home_budget
        home_budget = float(user_input['home_budget'])
        global state 
        state = user_input['state']
        state = state[0].upper() + state[1:]
    
    crime_rate_ntl_avg = np.mean(testinc['crime_rate_pc'])
    
    testinc = testinc.loc[(testinc['state'] == state) & (testinc['home_price'] < home_budget)]
    testinc.sort_values(by = 'residuals', ascending = False, inplace = True)
    
    best_deal = testinc.iloc[i]
    
    return render_template(
        'results1.html',
        townstate = best_deal['townstate'],
        actual_home_price = int(best_deal['home_price']),
        predicted_home_price = int(best_deal['preds']),
        crime_rate_pc = best_deal['crime_rate_pc'],
        relative_crime_rate = np.round(((crime_rate_ntl_avg - best_deal['crime_rate_pc']) / crime_rate_ntl_avg) * 100, 1),
        unemployment_rate = np.round(best_deal['unemployment_rate'], 2),
        median_income = int(best_deal['med_income'])
    )

if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run(debug=True)