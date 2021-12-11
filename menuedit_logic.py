import pymysql
import uuid
from werkzeug.utils import secure_filename
import os

db = pymysql.connect(host='localhost', db='kiosk', user='root', password='1234', charset='utf8')
cursor = db.cursor()

class menueditDao:
    def __init__(self):
        pass

    def menueditselect(self):
        ret = []

        sql = "select * from menu left join kiosk.menu_img on menu.menu_id = menu_img.menu_id"
        cursor.execute(sql)

        rows = cursor.fetchall()
        for e in rows:
            temp = {'menu_id': e[0], 'menu_name': e[1], 'menu_price': e[2], 'file_name': e[4]}
            ret.append(temp)

        db.commit()
        return ret

    def menueditimsiselect(self, menu_id):
        ret = []

        sql = "select * from menu where menu_id=%s;"
        cursor.execute(sql, menu_id)

        rows = cursor.fetchall()
        for e in rows:
            temp = {'menu_id': e[0], 'menu_name': e[1], 'menu_price': e[2]}
            ret.append(temp)

        db.commit()
        return ret

    def menueditimsi_imgselect(self, menu_id):
        ret = []

        sql = "select * from menu_img where menu_id=%s"
        cursor.execute(sql, menu_id)

        rows = cursor.fetchall()
        for e in rows:
            temp = {'file_id': e[0], 'file_name': e[1], 'original_filename': e[2], 'file_url': e[3], 'menu_id': e[4]}
            ret.append(temp)

        db.commit()
        return ret

    def menueditinsert(self, menuname, menuprice, menuimg):
        sql = "insert into menu (menu_name, menu_price) values(%s,%s)"
        cursor.execute(sql, (menuname, menuprice))
        db.commit()

        res = cursor.lastrowid
        imgname = str(uuid.uuid4()) + secure_filename(menuimg.filename)
        menuimg.save('static/menuimg/' + imgname)
        menuimg_files = os.listdir("static/menuimg/")

        sql1 = "insert into menu_img (file_name, original_filename, file_url, menu_id) values(%s, %s, %s, %s);"
        cursor.execute(sql1, (imgname, secure_filename(menuimg.filename), 'menuimg/' + secure_filename(menuimg.filename), res))
        db.commit()

    # def updEmp(self, empno, name, department, phone):
    #     sql = "update emp set name=%s, department=%s, phone=%s where empno=%s"
    #     cursor.execute(sql, (name, department, phone, empno))
    #     db.commit()
    #     db.close()

    def menueditdelete(self, menu_id):
        print("ddddd", menu_id)
        sql = "delete from menu where menu_id=%s"
        cursor.execute(sql, menu_id)
        db.commit()


# if __name__ == '__main__':
    # MyEmpDao().insEmp('aaa', 'bb', 'cc', 'dd')
    # MyEmpDao().updEmp('aa', 'dd', 'dd', 'aa')
    # menueditDao.menueditdelete('aaa')
    # menuList = menueditDao().menueditselect()
    # print(emplist)