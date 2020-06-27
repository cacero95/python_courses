import users.connection as dba
import datetime
import hashlib
# The next method return a list
# in the [0] the dba connection
# [1] the cursor
dba = dba.dba_network()
class User:
    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
    def register(self):
        date = datetime.datetime.now()
        sql = "insert into users(fullName, lastName, email, password, actualDate) values (%s,%s,%s,%s,%s)"
        # encode the password
        encode = hashlib.sha256()
        # The method update only encode a binary object
        # For that reason is neccesary convert the password to binary utf8
        encode.update(self.password.encode('utf8'))
        # encode.hexgigest() return the binary object at hexagesimal level
        # so at the moment when a login go with the same hexagesimal the dba will respond
        data = (self.name, self.lastname, self.email, encode.hexdigest(), date)
        
        try:
            dba[1].execute(sql,data)
            dba[0].commit()
            rows_count = dba[1].rowcount
            dba[0].close()
            return [rows_count, self]
        except Exception as error:
            return [0, error]
    def identificate(self):
        sql = "select * from users where email = %s and password = %s"
        # encode the password
        encode = hashlib.sha256()
        # The method update only encode a binary object
        # For that reason is neccesary convert the password to binary utf8
        encode.update(self.password.encode('utf8'))
        data = (self.email, encode.hexdigest())
        try:
            dba[1].execute(sql,data)
            result = dba[1].fetchone()
            out = [True, result] if result != None else [False, "the user was not found"]
            dba[0].close()
            return out
        except Exception as error:
            return [False, error]
