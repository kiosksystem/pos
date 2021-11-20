from flask import Flask

app = Flask(__name__)

@app.route("/", method=['GET', 'POST'])
def index():
    return render_template('Pos_main.html')