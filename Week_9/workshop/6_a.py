import random
import string

member_table = {"email1": "Blue", 
                "email2": "Fluffy", 
                "email3": "Smith",
                "email4": "Paris",
                "email5": "Michael"}

def generate_temp_password(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def update_password(email):
    temp_password = generate_temp_password(8)
    member_table[email] = temp_password
    print(f"Your temporary password is: {temp_password}")

update_password("email1")
print(member_table)
