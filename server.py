from flask import Flask #flask 모듈 import 
from flask import render_template

app = Flask(__name__) # flask name 선언 

@app.route("/", method=['GET', 'POST']) #flask 웹 페이지 경로 
def index(): # 경로에서 실행될 기능 선언 
    return render_template('Pos_main.html')

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=9000) # host주소와 port number 선언