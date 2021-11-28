import pymysql
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import menuedit_logic

app = Flask(__name__) # flask name 선언 

db = pymysql.connect(host='localhost', user='root', password='1234', db='kiosk', charset='utf8')
cursor = db.cursor()

@app.route("/") #flask 웹 페이지 경로 
def main(): # 경로에서 실행될 기능 선언 
    return render_template('Pos_main.html')

@app.route('/menuedit', methods=['GET', 'POST'])
def menuedit():
    if request.method == 'POST':
        menu_info = request.form
        menuname = menu_info['menu_nameTxt']
        menuprice = menu_info['menu_priceTxt']

        menu_img = request.files
        menuimg = menu_img['menu_img']

        menuedit_logic.menuedit(menuname, menuprice, menuimg)
    
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