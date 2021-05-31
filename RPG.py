import random
def RPG():
    length = int(input("Please enter the length of your password: "))
    password = " "
    for i in range(length):
        password += chr(random.randint(33, 126))
    print(password)

RPG()


