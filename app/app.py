from flask import Flask, render_template, request, url_for, redirect
from forms import *
from model import fit
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=["GET", "POST"])
def landing():
    title = 'Title'
    form = ParametersForm()
    form_name = 'Form name'
    if request.method == 'POST':
        data = request.form.get("param")
        return redirect(url_for('results', data=data))
    return render_template('landing.html', title = title, form = form, form_name = form_name)

@app.route('/results', methods=["GET", "POST"])
def results():
    title = 'Results'
    data = request.args.get("data")
    output = fit(data)
    return render_template('results.html', title = title, output = output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
