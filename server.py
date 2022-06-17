from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "password"


@app.route('/')
@app.route('/survey')
def display_form():
    return render_template("survey.html")


@app.route('/survey', methods=['POST'])
def create_user():
    print(request.form)
    if (display_results == None):
        return redirect('/survey')
    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comments'] = request.form['comments']
        return redirect("/result")	 


@app.route('/result')
def display_results():
    return render_template("survey_result.html")


if (__name__) == "__main__":
    app.run(debug=True)