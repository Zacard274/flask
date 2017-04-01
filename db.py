import  MySQLdb

#connect db
conn = MySQLdb.connect('localhost', 'root', '123456')

#get cursor
cur = conn.cursor()

#creat database
#cur.execute("""create database if not exists test""")
conn.select_db('test')

#create table
#cur.execute("""create table user (username varchar(32), password varchar(32)) """)

'''
sql = "select * from student"
inserSql = "insert into student (id,name) value (5, 'zhangsan')"

cur.execute(inserSql)
conn.commit()
cur.execute(sql)192.168.124.8

result = cur.fetchall()

for row in result:
    print row[0]
    print row[1]

conn.close()
'''
def addUser(username, password):
    sql = "insert into user (username, password) values('%s', '%s')" %(username,password)
    cur.execute(sql)
    conn.commit()
    conn.close()

def isExist(username, password):
    sql = "select * from user where username = '%s' and password = '%s'"%(username,password)
    cur.execute(sql)
    result = cur.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True




