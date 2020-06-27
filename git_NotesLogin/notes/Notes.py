import users.connection as dba


# The next method return a list
# dba.dba_network()
# in the [0] the dba connection
# [1] the cursor

class Notes:

    def __init__(self, id_user, title, path):

        self.id_user = id_user
        self.title = title
        self.path = path
        self.dba = dba.dba_network()
    def save_note(self):

        sql = "insert into notes (id_user, title, path, actualDate) values(%s,%s,%s, NOW())"
        data = (self.id_user, self.title, self.path)
        try:
            self.dba[1].execute(sql,data)
            self.dba[0].commit()
            rows_count = self.dba[1].rowcount
            self.dba[0].close()
            return [rows_count, self]
        except Exception as error:
            return [0, error]
    
    def show_notes(self):

        sql = f"select path from notes where id_user = {self.id_user}"
        
        try:
            self.dba[1].execute(sql)
            result = self.dba[1].fetchall()
            self.dba[0].close()
            return [True, result] if len(result) > 0 else [False, 0]
        except Exception as error:
            return [False, error]

    def delete_notes(self):

        sql = f"delete from notes where id_user = {self.id_user} and title = '{self.title}'"
        print(sql)
        try:
            self.dba[1].execute(sql)
            self.dba[0].commit()
            rows_count = self.dba[1].rowcount
            return [rows_count, self]
        except Exception as error:
            return [0, error]