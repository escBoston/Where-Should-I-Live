import numpy as np
import pandas as pd
import pickle
import re
from flask import Flask, request, Response, render_template

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

testinc = pd.read_csv('../data/testinc.csv')

app = Flask('Capstone')

@app.route('/form')

def form():
    return render_template('form1.html')

@app.route('/submit')

def submit():
    user_input = request.args
    print(*user_input, sep='\n')
    
    home_budget = float(user_input['home_budget'])
    state = user_input['state']
    
    return render_template('results.html')

if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run(debug=True)