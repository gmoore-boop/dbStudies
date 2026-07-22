import sqlite3 

def get_connection(db_name = 'library.db'):
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

conn = get_connection()
command = '''

drop table if exists authors
drop table if exists books

create table authors if not exists(
 id integer primary key, 
 name text not null
) strict 


create table books if not exists(
 id integer primary key, 
 title text not null,
 subject text not null, 
 author_id integer not null, 
 foreign key(author_id) references authors(id)
) strict 
'''
conn.execute(command)