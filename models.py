import sqlite3 as sql
from os import path

#this is the thin layer that allows server to interact with the database


ROOT = path.dirname(path.relpath((__file__)))

def create_post(name,content):
    #Connect to the database
    con = sql.connect(path.join(ROOT,'database.db'))
    #Create a cursor for efficient navigating the database
    cur = con.cursor()
    #Execute raw sql queries
    cur.execute('insert into posts (name,content) values(?,?)',(name,content))
    con.commit()
    con.close()

def get_posts():
    #display all the posts in this method
    con = sql.connect(path.join(ROOT,'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts
