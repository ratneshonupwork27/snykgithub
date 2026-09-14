# VULNERABLE: Evaluating raw user-supplied strings
user_input = input("Enter expression: ")
result = eval(user_input)  # An attacker can pass `__import__('os').system('id')`
print(result)
