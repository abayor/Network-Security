message = input("Please input your Message Here: \n")
translated = ""
i = len(message) - 1

while i > 0:
    translated = translated + message[i]
    i = i -1
print("Encrypting.....")
print(translated)

