import pymysql
from werkzeug.utils import secure_filename

db = pymysql.connect(host='localhost', db='kiosk', user='root', password='1234', charset='utf8')
cursor = db.cursor()

class mainDao:
    def __init__(self):
        pass

    def tableinsert(self, tablename):
        sql = "insert into table_list (table_name) values(%s)"
        cursor.execute(sql, tablename)
        db.commit()

    def tableselect(self):
        ret = []

        sql = "select * from table_list"
        cursor.execute(sql)

        rows = cursor.fetchall()
        for e in rows:
            temp = {'table_id': e[0], 'table_name': e[1]}
            ret.append(temp)

        db.commit()
        return ret

    def orderselect(self, table_id):
        ret = []

        sql = "SELECT order_id, table_id,menu_name,menu_price, sum(count) FROM kioskorder where table_id=%s group by menu_name;"
        cursor.execute(sql, table_id)

        rows = cursor.fetchall()
        for e in rows:
            temp = {'order_id': e[0], 'table_id': e[1], 'menu_name': e[2], 'menu_price': e[3], 'count': e[4]}
            ret.append(temp)

        db.commit()
        return ret
