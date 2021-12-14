import pymysql
from werkzeug.utils import secure_filename

db = pymysql.connect(host='localhost', db='kiosk', user='root', password='1234', charset='utf8')
cursor = db.cursor()

class calcDao:
    def __init__(self):
        pass

    def total_calc(self):
        ret = []

        sql = "select * from total_calc"
        cursor.execute(sql)

        rows = cursor.fetchall()
        for e in rows:
            temp = {'calc_id': e[0], 'time': e[1], 'total_result': e[2], 'table_id': e[3]}
            ret.append(temp)

        db.commit()
        return ret

    def total_detail(self, calc_id):
        ret = []

        sql = "select * from total_detail where calc_id=%s"
        cursor.execute(sql, calc_id)

        rows = cursor.fetchall()
        for e in rows:
            temp = {'id': e[0], 'table_id': e[1], 'menu_name': e[2], 'menu_price': e[3], 'count': e[4], 'result': e[5], 'calc_id': e[6]}
            ret.append(temp)

        db.commit()
        return ret
