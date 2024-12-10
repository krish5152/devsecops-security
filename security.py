# Example vulnerable code (SQL Injection)
username = input("Enter username:")
password = input("Enter password:")
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
print("Executing query:", query)
