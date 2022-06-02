from distutils.log import debug
from flask import Flask
from flask import render_template
app=Flask(__name__)


@app.route("/")
@app.route("/home")
def homepage():
    return render_template('home.html')


@app.route("/blog")
def blogpage():
    return render_template("blog.html")

@app.route("/post1")
def post1page():
    return render_template("post1.html")


@app.route("/post2")
def post2page():
    return render_template("post2.html")

@app.route("/post3")
def post3page():
    return render_template("post3.html")


@app.route("/register")
def registerpage():
   return render_template('register.html')

@app.route("/login")
def loginpage():
    return render_template('login.html')



if __name__=="__main__":
    app.run(debug=True)

