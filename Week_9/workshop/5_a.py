'''
password_lookup = {"username1": "password1", 
                  "username2": "password2", 
                  "username3": "password3", 
                  "username4": "password4", 
                  "username5": "password5"}
                  '''

password_lookup = {}
while True:
    username = input("Enter a username (or 'z' to exit): ")
    if username == 'z':
        break
    password = input("Enter a password: ")
    password_lookup[username] = password
print(password_lookup)
