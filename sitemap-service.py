import os

# VULNERABLE: Direct string formatting with user input
user_input = input("Enter a parameter: ")
command = f"echo Printing {user_input}"
os.system(command)  # If user inputs: "Hello; rm -rf /", it runs the rm command!
