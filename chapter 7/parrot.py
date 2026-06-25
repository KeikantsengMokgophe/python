#HOW THE INPUT FUNCTION WORK
# message = input("Tell me something, and I will repeat it back to you: hello everyone!")
# print(message)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
 message = input(prompt)
 print(message)

 if message != 'quit':
    print(message)