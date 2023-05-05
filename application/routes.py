
from application import app, db
from flask import Response, render_template, request
# from application.forms import LoginForm, RegisterForm



# classData = [{"classID": "101", "title": "Hot Yoga", "instructor": "Kim", "duration": "60"},{"classID": "102", "title": "Group Yoga", "instructor": "Alex", "duration": "55"},
#                  {"classID": "103", "title": "Individual Yoga", "instructor": "Tonya", "duration": "70"},{"classID": "104", "title": "Outdoor Yoga", "instructor": "TBD", "duration": "65"},
#                  ]





@app.route("/")
def index():
    return render_template("index.html", index=True)




@app.route("/register")
def register():
    return render_template("register.html")



@app.route("/about")
def about():
    return render_template("about.html")


class User(db.Document):
        user_id = db.IntField( unique=True )
        first_name = db.StringField(max_length=50)
        last_name = db.StringField(max_length=50)
        email = db.StringField(max_length=30)
        password = db.StringField(max_length=30)




@app.route("/user")
def user():
    User(user_id=1, first_name="Jace", last_name="Goat", email="jace@gmail.com", password="foot1234").save()
    users = User.objects.all()
    return render_template("user.html", users=users)



