import mysql.connector as connect
from users import actions

print("""
    1 or register
    2 or login
""")
chooise = actions.Actions()
action = input("What do you need: ")

if action == "register" or action == "1":
    chooise.register()
elif action == "login" or action == "2":
    chooise.login()
else:
    exit()