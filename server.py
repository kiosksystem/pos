from flask.helpers import url_for
import pymysql
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from menuedit_logic import menueditDao
from main_logic import mainDao

app = Flask(__name__) 

db = pymysql.connect(host='localhost', user='root', password='1234', db='kiosk', charset='utf8')
cursor = db.cursor()

@app.route("/", methods=['GET', 'POST'])
def main(): 
    tableList = mainDao().tableselect()
    orderList = []
    ordercalc = []

    if request.method == 'POST':
        menu_info = request.form
        gettableinfo = list(menu_info.values())
        strtableinfo = "".join(gettableinfo)
        table_id = strtableinfo.split("-")

        orderList = mainDao().orderselect(table_id[1])

    return render_template('Pos_main.html', tableList=tableList, orderList=orderList)

@app.route("/addTable", methods=['GET', 'POST'])
def addTable():
    tablename = "table"
    mainDao().tableinsert(tablename)
    
    return redirect("/")


@app.route('/menuedit', methods=['GET', 'POST'])
def menuedit():
    menuList = menueditDao().menueditselect()

    if request.method == 'POST':
        menu_info = request.form
        menuimsilist = list(menu_info.values())
        imsimenulist = menueditDao().menueditimsiselect(menuimsilist)
        imsimenuimg = menueditDao().menueditimsi_imgselect(menuimsilist)

        return render_template('Pos_menuEdit.html', menuList=menuList, imsimenulist=imsimenulist, imsimenuimg=imsimenuimg)

    return render_template('Pos_menuEdit.html', menuList=menuList)

@app.route('/menueditinsert', methods=['GET', 'POST'])
def menueditinsert():
    if request.method == 'POST':
        menu_info = request.form
        menuname = menu_info['menu_nameTxtRight']
        menuprice = menu_info['menu_priceTxtRight']

        menu_img = request.files
        menuimg = menu_img['menu_img']

        menueditDao().menueditinsert(menuname, menuprice, menuimg)

    return redirect('/menuedit')

@app.route('/menueditdelete', methods=['GET', 'POST'])
def menueditdelete():
    if request.method == 'POST':
        menu_info = request.form

        q = list(menu_info.values())

        menueditDao().menueditdelete(q[0])

    return redirect('/menuedit')

@app.route('/calc')
def calc():
    return render_template('Pos_calculate.html')

@app.route("/addmenu")
def addmenu():
    return render_template('Pos_Addmenu.html')

if __name__ == "__main__":
    app.run(debug=True) 
    # app.run(host="0.0.0.0", port=9000) # host주소와 port number 선언