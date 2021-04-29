
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Hello!"

def index():
    if request.method == 'POST':
        print(request.form.getlist('hello'))

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
