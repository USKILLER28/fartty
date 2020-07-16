from flask import Flask, render_template

app = Flask(__name__)


@app.route('/',)
def index():
    return '<a href="http://127.0.0.1:5000/chat"><button>chat</button></a>'


if __name__ == "__main__":
    app.run(debug=True)


