import sqlite3 

def get_connection(db_name = 'library.db'):
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

conn = get_connection()
start = '''
drop table if exists books;
drop table if exists authors;

create table if not exists authors(
 id integer primary key, 
 name text not null
) strict;


create table if not exists books(
 id integer primary key, 
 title text not null,
 subject text not null, 
 author_id integer not null, 
 foreign key(author_id) references authors(id)
) strict;
'''
#solved syntax error. Table name should be after all statements

conn.executescript(start) #execute() only process one statement at a time

def add_author(conn, id, name):
    conn.execute('''
        insert into authors(id, name) values(?,?)
    ''', [id, name])

def add_book(conn, id, title, subject, author_id):
    conn.execute('''
        insert into books(id, title, subject, author_id) values(?, ?, ?, ?)
    ''', [id, title, subject, author_id])

add_author(conn, 1, "J.R.R. Tolkien")
add_author(conn, 2, "Frank Herbert")
add_author(conn, 3, "Mary Shelley")
add_author(conn, 4, "George Orwell")
add_author(conn, 5, "Agatha Christie")
add_author(conn, 6, "Isaac Asimov")

add_book(conn, 101, "The Hobbit", "Fantasy", 1)
add_book(conn, 102, "The Fellowship of the Ring", "Fantasy", 1)
add_book(conn, 103, "Dune", "Science Fiction", 2)
add_book(conn, 104, "Dune Messiah", "Science Fiction", 2)
add_book(conn, 105, "Frankenstein", "Gothic Horror", 3)
add_book(conn, 106, "1984", "Dystopian", 4)
add_book(conn, 107, "Animal Farm", "Political Satire", 4)
add_book(conn, 108, "Murder on the Orient Express", "Mystery", 5)
add_book(conn, 109, "And Then There Were None", "Mystery", 5)
add_book(conn, 110, "Foundation", "Science Fiction", 6)
add_book(conn, 111, "I, Robot", "Science Fiction", 6)

