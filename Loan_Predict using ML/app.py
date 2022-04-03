import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import re
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
model = pickle.load(open('LoanFinal.pickle', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(x) for x in request.form.values()]
    final_feature = [np.array(input_data)]
    prediction = model.predict(final_feature)
    output = np.around(prediction)
    if output == 1:
        output = "yes"
    elif output == 0:
        output = "No"
    return render_template('home.html', prediction_text='Loan Approval status : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)

https://www.youtube.com/watch?v=Zy_hZVLXVqw