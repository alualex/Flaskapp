
from flask import Flask, render_template, request

app = Flask(__name__)

items = {"Alice":20, "Vijin":21}
vij = {10000, 2000}
@app.route('/')
@app.route("/index.html")
def hello():
    return render_template('index.html',items = vij)


@app.route("/vijin")

def button():
    return "<button type='button' onclick='alert('Hi user!')'>Press me!</button>"


@app.route("/alice")
def hello2():
    return "<h1> This is a button Vijin: {} </h1> <button type = 'button'> Status</button>".format(items["Alice"])




if __name__ == "__main__":
    app.run(debug=True)

