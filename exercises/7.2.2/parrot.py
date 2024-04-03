prompt = "Tell me something, and I'll repeat it to you:"
prompt += "\nEnter 'quit' to stop the program."
message = ''

while message != 'quit':
    message = input(prompt)
    print(message)