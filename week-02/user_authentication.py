def user_authentication(user, passw):
    existing_user = "ehsaslab"
    existing_pass = "ehsaslab"
    if existing_user == user and existing_pass == passw:
        return True
    elif existing_user == user and existing_pass != passw:
        return "Invalid Password!"
    elif existing_user != user and existing_pass == passw:
        return "Invalid username"
    else:
        return "Invalid credentials"

print(user_authentication('ehsaslab', 'ehsaslab')) # True
print(user_authentication('ali', 'ehsaslab')) # Invalid username
print(user_authentication('ehsaslab', 'ali')) # Invalid Password!
print(user_authentication('ali', 'ali')) # Invalid credentials