#-------------------DB Connecct-----------------------
# import mysql.connector as myCon
# m=myCon.connect(host='localhost',user='root',password='root')
# print("DB connect:",m)

import mysql.connector as mysql
dbCon=mysql.connect(host='localhost',user='root',password='root', database='python')
db=dbCon.cursor()
'''-----------------------------Table create----------------------'''
# db.execute("create table user(id int auto_increment not null primary key,name varchar(20),branch varchar(20))")
# print("table created")

'''--------------------------table show-----------------------'''
db.execute("show tables")
for i in db:
    print(i)

'''---------------------------SINGLE data insert---------------------------------'''
# db.execute("insert into user(name,branch) values('ishor','cs')")
# print(db.rowcount,": row inserted")
# print(db.rowcount,": row inserted")

"""--------------------insert MULTIPLE Data-----------------------------"""
# q="insert into user(name,branch) values(%s,%s)"
# list=[("ram","cs"),("kumar","civil")]
# db.executemany(q,list)
# print(db.rowcount,": row inserted")
# dbCon.commit()

'''-------------------Table DATA show---------------------------'''
db.execute("select *from user")
# data=db.fetchall()
# print(data)

for i in db.fetchall():
    print(i)


'''-------------------Update Data------------------------'''
# q="update user set name=%s where id=%s"
# value=('kumar',1)
# db.execute(q,value)
# dbCon.commit()
# print("update")


'''-------------------Delete Data----------------------'''
q='delete from user where id=%s'
val=[4]
db.execute(q,val)
dbCon.commit()
print("delete")