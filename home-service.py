# Vulnerability: Executing raw user input directly
user_input = input("Enter an expression: ")
result = eval(user_input)  # Unsafe!
print(result)
