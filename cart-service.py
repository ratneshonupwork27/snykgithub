import subprocess
username = input("Enter username: ")
# Unsafe: shell=True allows command chaining/injection if input is unescaped
subprocess.run(f"echo {username}", shell=True) 
