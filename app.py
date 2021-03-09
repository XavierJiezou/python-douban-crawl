from flask import Flask, render_template
import sqlite3
import jieba
app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index.html')


@app.route('/index',methods=['get','post'])
def index():
    return render_template('index.html')


@app.route("/movie")
def movie():
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    sql = 'select * from douban'
    data = list(cur.execute(sql))
    head = [i[0] for i in cur.description]
    data.insert(0, head)
    cur.close()
    con.close()
    return render_template('movie.html', data=data)


# @app.route("/movie/<int:page>")
# def movie_page(page):
#     con = sqlite3.connect('test.db')
#     cur = con.cursor()
#     sql = 'select * from douban'
#     data = list(cur.execute(sql))
#     head = [i[0] for i in cur.description]
#     data.insert(0, head)
#     cur.close()
#     con.close()
#     return render_template('movie.html', data=data, page=page)


@app.route("/score")
def score():
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    sql = 'select score,count(score) from douban group by score'
    data = list(cur.execute(sql))
    cur.close()
    con.close()
    score = [item[0] for item in data]
    count = [item[1] for item in data]
    return render_template('score.html', score=score, count=count)


@app.route("/word")
def word():
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    sql = 'select quote from douban'
    dat = cur.execute(sql)
    txt = ''
    for item in dat:
        txt += item[0]
    words = jieba.cut(txt)
    cur.close()
    con.close()
    dict = {}
    for word in words:
        if len(word) == 1:
            continue
        dict[word] = dict.get(word,0)+1
    data = list(dict.items())
    # data.sort(key=lambda x:x[1],reverse=True)
    return render_template('word.html',data=data)


@app.route("/team")
def team():
    return render_template('team.html')


if __name__ == "__main__":
    app.run(debug=True)
