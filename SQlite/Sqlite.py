import sqlite3

#connection

# Open the connection
connection = sqlite3.connect('test.db')

# Cursor Create

cursor = connection.cursor()

# Create table
## The autoincrement have to go beside a primary key or deploy a error
cursor.execute("""CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title varchar(255),
    description text,
    precio int(255)
)""")


# insert data
cursor.execute("INSERT INTO products (title, description, precio) values ('my first title', 'have to take commits', 2020) ")
# delete objects
cursor.execute('delete from products')
# inserts many objects
many_products = [
    ('second title', 'second description', 2021),
    ('third title', 'second description', 2021),
    ('four title', 'second description', 2021),
    ('five title', 'second description', 2022)
]
# the first param is the query and the second param is the data at this case is a tuple
cursor.executemany("insert into products (title,description, precio) values(?,?,?)", many_products)
# update data
cursor.execute("update products set precio = 10000 where precio=2021")

# select data
cursor.execute("select * from products where precio > 100")
products = cursor.fetchall()

for product in products:
    print(product)
    print(product[1])

# get the first object at the query
product = cursor.fetchone()
print(product)


# save changes
connection.commit()
# Close the connection
connection.close()

