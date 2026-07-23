import tabulate
from main import get_connection

conn = get_connection()

result = conn.execute('''
    select books.title, books.subject, authors.name 
    from books
    join authors on books.author_id = authors.id
    ''')

print(tabulate.tabulate(result.fetchall(),['title', 'subject', 'author'], 'rounded_grid'))



