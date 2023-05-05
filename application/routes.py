
from application import app
from flask import Response, render_template, request, json
from flask_pymongo import pymongo
from application.models import User, Yoga, Enrollment

from os import environ


classData = [{"classID": "101", "title": "Hot Yoga", "instructor": "Kim", "duration": "60"},{"classID": "102", "title": "Group Yoga", "instructor": "Alex", "duration": "55"},
                 {"classID": "103", "title": "Individual Yoga", "instructor": "Tonya", "duration": "70"},{"classID": "104", "title": "Outdoor Yoga", "instructor": "TBD", "duration": "65"},
                 ]


CONNECTION_STRING = environ.get('MONGODB')
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('classes')
user_collection = pymongo.collection.Collection(db, 'user_collection')



@app.route("/")
def index():
    return render_template("index.html", index=True)



@app.route("/courses")
def courses():
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

@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = request.form.get('classID')
    title = request.form.get('title')
    duration = request.form.get('duration')
    return render_template("enrollment.html", enrollment=True, data={"id": id, "title": title, "duration": duration})


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = classData 
    else:
        jdata = classData[int(idx)]
    
    return Response(json.dumps(jdata), mimetype="application/json")



app.route("/user")
def user():
    if request.method == 'POST':
        users = db.users
        existing_user = users.find_one({'email': request.form['email']})
        if existing_user is None:
            users.insert_one({'email': request.form['email'], 'first_name': request.form['first_name'], 'password': request.form['password'], 'last_name': request.form['last_name']})

   
    return render_template("user.html", users=users)



