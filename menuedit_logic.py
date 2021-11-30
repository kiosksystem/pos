import pymysql
from flask import request, redirect
from werkzeug.utils import secure_filename
import uuid

import os

db = pymysql.connect(host='localhost', user='root', password='1234', db='kiosk', charset='utf8')
cursor = db.cursor()

def menueditadd(menuname, menuprice, menuimg):
    sql = "INSERT INTO menu (menu_name, menu_price) VALUES (%s, %s);"
    cursor.execute(sql, (menuname, menuprice))
    db.commit()
    
    res = cursor.lastrowid
    imgname = str(uuid.uuid4()) + secure_filename(menuimg.filename)
    menuimg.save('static/menuimg/' + imgname)
    menuimg_files = os.listdir("static/menuimg/")

    sql1 = "INSERT INTO menu_img (file_name, original_filename, file_url, menu_id) VALUES(%s, %s, %s, %s);"
    cursor.execute(sql1, (imgname, secure_filename(menuimg.filename), 'menuimg/'+secure_filename(menuimg.filename), res))
    db.commit()

def menueditselect():
    sql = "SELECT * FROM menu left join menu_img on menu.menu_id = menu_img.menu_id;"
    cursor.execute(sql)

    rows = cursor.fetchall()
    
    return rows


