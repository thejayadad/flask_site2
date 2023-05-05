

from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask.json import JSONEncoder


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'YOGA_Studio',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)


from application import routes



if __name__ == "__main__":
    app.run(debug=True)



