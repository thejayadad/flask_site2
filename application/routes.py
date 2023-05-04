
from application import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html", index=True)



@app.route("/courses")
def courses():
    classData = [{"classID": "101", "title": "Hot Yoga", "instructor": "Kim", "duration": "60"},{"classID": "102", "title": "Group Yoga", "instructor": "Alex", "duration": "55"},
                 {"classID": "103", "title": "Individual Yoga", "instructor": "Tonya", "duration": "70"},{"classID": "104", "title": "Outdoor Yoga", "instructor": "TBD", "duration": "65"},
                 ]
    return render_template("courses.html", classData = classData, courses=True)



@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html", login=True)


@app.route("/about")
def about():
    return render_template("about.html")