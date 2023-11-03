# onederfull-python

## class
- https://wikidocs.net/16071

## pymysql 구조
- http://pythonstudy.xyz/python/article/202-MySQL-%EC%BF%BC%EB%A6%AC
```py
conn = pymysql.connect()
cur = conn.cursor()
cur.execute()
cur.fetchall() # only for select
conn.commit()
conn.close()
```
### example
```py
import pymysql
conn = pymysql.connect(host = config.host,
                             port = config.port,
                             user = config.user,
                             password = config.password,
                             db = config.db,
                             charset = config.charset
                             )
try:
    with conn.cursor() as cursor:
        sql = 'select * from table'
        cursor.execute(sql)
        result = cursor.fetchall()
    conn.commit()
finally:
    conn.close()
```

## data model
- eng. https://docs.python.org/3/reference/datamodel.html
- kor. https://docs.python.org/ko/3/reference/datamodel.html

## Datetime
- https://hazel01.tistory.com/34
