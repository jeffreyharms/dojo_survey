from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "password"

@app.route('/')
@app.route('/Home')
def display_form():
    return render_template("survey.html")

@app.route('/submit', methods=['POST'])
def create_user():
    print("Got Post Info")
    # print(request.form)
    # name = request.form['name']
    # email = request.form['email']
    return redirect("/result")	 
    
@app.route('/result')
def show_ninja(your_name, dojo_location, favorite_language, comments):
    print("Showing the User Info From the Form")
    # print(request.form)
    return render_template("survey_result.html", your_name = your_name, dojo_location = dojo_location, favorite_language = favorite_language, comments = comments)

if (__name__) == "__main__":
    app.run(debug=True)