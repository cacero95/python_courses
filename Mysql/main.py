import mysql.connector as connect

## create database
try:
    dba = connect.connect(
        host="localhost",
        user="root",
        passwd="",
        database="master_python"
    )
    cursor = dba.cursor(buffered=True) ## this param is neccesary in case of multiples queries
except:
    dba = connect.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    cursor = dba.cursor(buffered=True)
    cursor.execute(
        """
            create database id not exists master_python
        """
    )
# for make query is necessary create a cursor

# for show the all the dba
cursor.execute("show databases")
for db in cursor:
    print(db)
# Create tables
# 10,2 its means 10 digits and 2 decimals
cursor.execute(
    """
        create table if not exists cars(
            id int(10) auto_increment not null,
            brand varchar(40) not null,
            model varchar(40) not null,
            price float(10,2) not null,
            CONSTRAINT pk_cars primary key(id)
        )
    """
)
cursor.execute("show tables")
# show tables
print("Show tables at cars\n")
for table in cursor:
    print(table)
# insert into tables
cursor.execute("insert into cars(brand, model, price) values( 'mazda', 'rx7', 3000000 ) ")

# insert multiples objects

cars = [
    ('mercedes', 'blr', '35000'),
    ('clio', 'blr', '25000'),
    ('pichirilo', 'blr', '10000')
]
cursor.executemany("insert into cars(brand, model, price) values( %s, %s, %s )", cars)

dba.commit()
## select objects
cursor.execute("select * from cars")
## cursor.fetchone() list the first object in the query
result = cursor.fetchall()
print('--------list all the cars--------')
for car in result:
    print(car)
## delete objects
cursor.execute("delete from cars where model = 'blr'")
## the delete needs the commit
dba.commit()
# print the number of used objects after a query
print(cursor.rowcount, "deleted")

# update objects

cursor.execute("update cars set price=2000 where price > 1000")
dba.commit()
print(cursor.rowcount, "updated")