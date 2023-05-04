
from application import app


@app.route("/")
def index():
    return "<h2>heyy</h2>"



