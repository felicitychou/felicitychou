


```
import psycopg2

conf = {"host":'127.0.0.1', "port":5432, "database":"", "user":"", "password":""}

conn = psycopg2.connect(**conf)
conn.set_session(autocommit=True) # 设置自动提交
cur = conn.cursor()

# 查询
sql = r"SELECT * FROM TABLE"

cur.execute(sql) # execute(query, vars=None)
cur.fetchone() # 返回一条结果(类型为元组)，如果找不到，返回none。
cur.fetchmany(1000) # 返回所有结果，类型为列表，如果找不到，返回空list.。
cur.fetchall() # 调用时需要指定返回结果数的参数， 每次调用，游标向后移，返回值如同fetchall()。
返回[(col1,),(col2)]

# 增删改
>>> cur.execute("""INSERT INTO some_table (an_int, a_date, a_string) VALUES (%s, %s, %s);""",(10, datetime.date(2005, 11, 18), "O'Reilly"))
>>> cur.execute("INSERT INTO foo VALUES (%s)", ("bar",)) # correct
>>> cur.execute("INSERT INTO foo VALUES (%s)", ["bar"])  # correct
sql = "UPDATE TABLE SET col1 = var1 where col2 = var2""

cur.executemany(query, vars_list)
cur.mogrify(sql) # 可以查看构造的SQL语句
conn.commit() # 需要提交

cur.close()
conn.close()

``