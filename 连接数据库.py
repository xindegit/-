import pymysql


class MysqlDB:
    def __init__(self):
        # 创建db对象
        self.db = pymysql.connect(
            host="rm-cn-9lb3ehybn000c47o.rwlb.rds.aliyuncs.com",
            port=3306,
            user="root",
            password="aliyun666+",
            database="bokeyuan"
        )
        # 创建游标
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def get_data(self, sql, args=None):
        self.cursor.execute(sql, args)
        data = self.cursor.fetchall()
        return data

    def set_data(self, sql, args=None):
        self.cursor.execute(sql, args)
        # 统一提交
        self.db.commit()

    def __del__(self):
        self.db.close()
