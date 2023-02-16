from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "徐偉騰超欠揍的~"


def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
