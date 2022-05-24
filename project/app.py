from distutils.log import debug
from flask import Flask
from flask import render_template
app=Flask(__name__)


@app.route("/")
@app.route("/home")
def homepage():
    return 'this is home page'


@app.route("/blog")
def blogpage():
    return ' this is blog page '

@app.route("/post1")
def post1page():
    return 'thi is post page 1'


@app.route("/post2")
def post2page():
    return 'thi is post page '

@app.route("/post3")
def post3page():
    return 'thi is post page 3'


@app.route("/register")
def registerpage():
   return render_template('register.html')

@app.route("/login")
def loginpage():
    return render_template('login.html')



if __name__=="__main__":
    app.run(debug=True)

