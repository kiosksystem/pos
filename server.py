from flask import Flask #flask 모듈 import 
from flask import render_template
import menuedit_logic

app = Flask(__name__) # flask name 선언 

@app.route("/") #flask 웹 페이지 경로 
def main(): # 경로에서 실행될 기능 선언 
    return render_template('Pos_main.html')

@app.route('/menuedit')
def menuedit():
    menuedit_logic.menuedit()
    return render_template('Pos_menuEdit.html')
    
@app.route('/calc')
def calc():
    return render_template('Pos_calculate.html')

@app.route("/addmenu")
def addmenu():
    return render_template('Pos_Addmenu.html')

if __name__ == "__main__":
    app.run(debug=True) 
    # app.run(host="0.0.0.0", port=9000) # host주소와 port number 선언