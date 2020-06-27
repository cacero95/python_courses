import users.User as Model
import notes.actions

class Actions:
    def register(self):

        print("\nOk lets register in the system")
        name = input('What is your name? ')
        lastName = input('What is your last name? ')
        email = input('What is your email? ')
        password = input('Give it a password? ')
        
        user = Model.User(name, lastName, email, password)
        register = user.register()
        print(f"\nUser {name} registered with the email {email}") if register[0] > 0 else print(f"\nAn error was ocurred {register[1]}")
    
    def login(self):
        print("Login in the system please")
        email = input('What is your email?: ')
        password = input('What is the password?: ')

        user = Model.User('', '', email, password)
        login = user.identificate()
        if login[0] == False:
            print(f"\nAn Error Ocurred {login[1]}")
        else:
            print(f"\n Welcome {login[1][1]} email {login[1][3]}")
            self.next_steps(login[1][0])
    def next_steps(self, user):
        print("""
            Available actions
            - 1 or Create notes (create)
            - 2 or Show your notes (show)
            - 3 or Delete notes (delete)
            - 4 or Exit (exit)
        """)
        action = input("What do you need \n")
        funtions = notes.actions.Actions()
        if action == "create" or action == "1":
            funtions.create(user)
            self.next_steps(user)
        elif action == "show" or action == "2":
            print('------')
            funtions.show(user)
            self.next_steps(user)
        elif action == "delete" or action == "3":
            funtions.delete(user)
            self.next_steps(user)
        else:
            print("Get out of here")
            exit()