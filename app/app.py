from flask import Flask, render_template, request, url_for
from forms import *
from model import *

app = Flask(__name__)

@app.route('/')
def landing():
    title = 'Title'
    form = ParametersForm()
    form_name = 'Form name'
    if form.validate_on_submit():
        return redirect(url_for('results', data=form.param))
    return render_template('templates/landing.html', title = title, form = form, form_name = form_name)

@app.route('/results')
def results():
    data = request.args.get("data")
    output = model(data)
    return render_template('templates/results.html', output = output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
