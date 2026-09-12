# VULNERABLE
user_input = input("Enter math expression: ")
result = eval(user_input)  # An attacker can input: __import__('os').system('rm -rf /')
