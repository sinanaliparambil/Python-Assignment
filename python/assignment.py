users = []

def create_user(username, password, active):
    new_user = {
        "username": username,
        "password": password,
        "active": active
    }
    users.append(new_user)
    print("User created successfully!")

    def get_all_users():
    return users

    def update_user(index, updated_user):
    users[index] = updated_user
    print("User updated successfully!")

    def delete_user(index):
    del users[index]
    print("User deleted successfully!")

    create_user("Alice", "password123", True)
create_user("Bob", "secret456", False)

print(get_all_users())

# Update Alice's password
updated_user = {"username": "Alice", "password": "new_password", "active": True}
update_user(0, updated_user)

print(get_all_users())

# Delete Bob
delete_user(1)

print(get_all_users())