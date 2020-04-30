from flask import Flask, render_template, request, url_for, redirect
from forms import *
from model import fit
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def landing():
    title = 'Title'
    form = ParametersForm()
    form_name = 'Form name'
    return render_template('landing.html', title = title, form = form, form_name = form_name)

@app.route('/results', methods=['POST'])
def results():
    title = 'Results'
    param = request.form['param']
    output = fit(param)
    return render_template('results.html', title = title, output = output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
