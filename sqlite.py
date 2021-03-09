'''
course link: https://www.runoob.com/sqlite/sqlite-python.html
'''


import sqlite3
from tqdm import tqdm


'''
create
'''
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
# sql = '''
#     create table douban(
#         id integer primary key autoincrement,
#         title text,
#         score real, 
#         comment int,
#         quote text,
#         year int,
#         country text,
#         category text,
#         link text,
#         cover text
#     )
# '''
# cursor.execute(sql)


'''
insert
'''
# f = open('douban.csv','r',encoding='utf_8_sig')
# data = f.readlines()
# f.close()
# for item in tqdm(data[1:]):
#     item = ['"'+i+'"' for i in item[:-1].split(',')]
#     try:
#         sql = '''
#             insert into douban (title, score, comment, quote, year, country, category, link, cover) 
#             values(%s)
#         '''%','.join(item)
#         cursor.execute(sql)
#     except Exception as e:
#         print(e)


'''
select
'''
# sql = 'select * from douban'
# data = cursor.execute(sql)
# for row in list(data)[:3]:
#     print(row)
# values = cursor.fetchall()
# print(len(values))


'''
close
'''
cursor.close()
conn.commit()
conn.close()