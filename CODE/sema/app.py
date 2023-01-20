from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from scrapper import parser
from tomita.tomita import tomita
from spark_app.words import spark
import sqlite3


app = Flask(__name__, template_folder='templates')

con = sqlite3.connect("sema.db")    


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/parser")
def func_parser():
    parser()
    return render_template("scrapper.html")


@app.route("/posts")
def posts():
    try:
        with sqlite3.connect("sema.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM post ORDER BY date DESC LIMIT 50")
            posts = cur.fetchall()
    except:
        con.rollback()
    finally:
        return render_template("posts.html", posts = posts)


@app.route("/posts/<int:id>")
def post_detail(id):
    try:
        with sqlite3.connect("sema.db") as con:
            cur_props = con.cursor()
            cur_props.execute("SELECT * FROM props WHERE id_post = "+ str(id))
            props = cur_props.fetchall()
            cur_post = con.cursor()
            cur_post.execute("SELECT text, date FROM post WHERE id_post = "+ str(id))
            post = cur_post.fetchone()
            
            if len(props) == 0: 
                tomita(post[0], id, post[1])
                cur = con.cursor()
                cur.execute("SELECT * FROM props WHERE id_post = "+ str(id))
                props = cur.fetchall()
    except:
        con.rollback()
    finally:
        return render_template("post_detail.html", props = props, post = post[0])


@app.route("/avarage", methods=["POST", "GET"])
def avarage():
    if request.method == "POST":
        try:
            with sqlite3.connect("sema.db") as con:
                ot = request.form["ot"]
                do = request.form["do"]
                cur_avarage_date = con.cursor()
                cur_avarage_date.execute("SELECT facts, COUNT(CASE WHEN tonality='Positive' THEN 1 ELSE NULL END) as pos, COUNT(CASE WHEN tonality='Negative' THEN 1 ELSE NULL END) as neg FROM props WHERE NOT facts = '-' AND DATE(dates) > '" + str(ot) + "' AND DATE(dates) < '" + str(do) + "' GROUP BY facts")
                allFacts = cur_avarage_date.fetchall()
                return render_template("avarage.html", allFacts = allFacts)        
        except:
            cur_avarage = con.cursor()
            cur_avarage.execute("SELECT facts, COUNT(CASE WHEN tonality='Positive' THEN 1 ELSE NULL END) as pos, COUNT(CASE WHEN tonality='Negative' THEN 1 ELSE NULL END) as neg FROM props WHERE NOT facts = '-' GROUP BY facts")
            allFacts = cur_avarage.fetchall()
            con.rollback()
    else:
        try:
            with sqlite3.connect("sema.db") as con:
                cur_avarage = con.cursor()
                cur_avarage.execute("SELECT facts, COUNT(CASE WHEN tonality='Positive' THEN 1 ELSE NULL END) as pos, COUNT(CASE WHEN tonality='Negative' THEN 1 ELSE NULL END) as neg FROM props WHERE NOT facts = '-' GROUP BY facts")
                allFacts = cur_avarage.fetchall()
                return render_template("avarage.html", allFacts = allFacts)     
        except:
            con.rollback()


@app.route("/allProps")
def allProps():
    try:
        with sqlite3.connect("sema.db") as con:
            cur_all = con.cursor()
            cur_all.execute("SELECT id_post, text, date FROM post ORDER BY date DESC")
            all_data = cur_all.fetchall()
            for item in all_data:
                tomita(item[1], item[0], item[2])
        return render_template("allprops.html")
    except:
        msg = 'not success'


@app.route("/spark", methods=["POST", "GET"])
def synonims():
    if request.method == "POST":
        word = request.form["word"]
        words = spark(word.lower())
        if words == 'notExist':
            return render_template("spark.html")
        else:
            return render_template("spark.html", words=words)
    else:
        return render_template("spark.html")





if __name__ == "__main__":
    app.run(debug=True)