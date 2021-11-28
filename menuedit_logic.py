import pymysql
from flask import request, redirect
from werkzeug.utils import secure_filename
import uuid

import os

db = pymysql.connect(host='localhost', user='root', password='1234', db='kiosk', charset='utf8')
cursor = db.cursor()

def menuedit(menuname, menuprice, menuimg):
    sql = "INSERT INTO menu (menu_name, menu_price) VALUES (%s, %s);"
    cursor.execute(sql, (menuname, menuprice))
    db.commit()
    
    res = cursor.lastrowid
    menuimg.save('static/menuimg/' + str(uuid.uuid4()) + secure_filename(menuimg.filename))
    menuimg_files = os.listdir("static/menuimg/")

    sql1 = "INSERT INTO menu_img (file_name, original_filename, file_url, userid) VALUES(%s, %s, %s, %s);"
    cursor.execute(sql1, (str(uuid.uuid4()) + secure_filename(menuimg.filename), secure_filename(menuimg.filename), 'menuimg/'+secure_filename(menuimg.filename), res))
    db.commit()

