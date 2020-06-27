import mysql.connector as connect

def dba_network():
    dba = connect.connect(
        host="localhost",
        user="root",
        passwd="",
        database="master_python",
        port=3306
    )
    cursor = dba.cursor(buffered=True)
    return [dba,cursor]