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

        sql = "select order_id, table_id,menu_name,menu_price, sum(count) as count, menu_price*count as result FROM kioskorder where table_id=%s group by menu_name;"
        cursor.execute(sql, table_id)

        rows = cursor.fetchall()
        for e in rows:
            temp = {'order_id': e[0], 'table_id': e[1], 'menu_name': e[2], 'menu_price': e[3], 'count': e[4], 'result': e[5]}
            ret.append(temp)

        db.commit()
        return ret

    def addTotal_calc(self, current_time, orderList):
        sql = "insert into total_calc(time) values(%s);"
        cursor.execute(sql, current_time)
        db.commit()

        res = cursor.lastrowid

        for i in range (0, len(orderList)):
            orderList[i]['calc_id'] = res

        for i in range (0, len(orderList)):
            del orderList[i]['order_id']

        sql1 = "insert into ex(table_id, menu_name, menu_price, count, result, calc_id) values (%s, %s, %s, %s, %s, %s);"
        cursor.executemany(sql1, orderList)
        db.commit()