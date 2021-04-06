import pymysql
class SqlUtil(object):
    def __init__(self):
        self.connect=pymysql.connect(host="120.24.33.253",user='root',password='123456',charset='utf8',database='apple')
        self.cus=self.connect.cursor(cursor=pymysql.cursors.DictCursor)
    def __del__(self):
        self.cus.close()
        self.connect.close()

    def findall(self,sql):
        self.cus.execute(sql)
        return self.cus.fetchall()

if __name__ == '__main__':
    print(SqlUtil().findall('select * from `member`;')[-1]['Id'])

