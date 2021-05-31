def calculate():
    number1 = int(input("Please enter your first number: "))
    number2 = int(input("Please enter your second number: "))
    option = input("Please pick a number from 1 to 4: ")
    if option == "1":
        print(number1 + number2) 
    elif option == "2":
        print(number1 - number2)
    elif option == "3":
        print(number1*number2)
    elif option == "4":
        print(number1/number2)
    else:
        print("Cannot be computed")

calculate()
