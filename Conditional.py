i = 8
if(i % 2 == 0):
    print("Even number")
else:
    print("Odd number")
# % is the modulo sign. It returns the remainder of the number
 
# def evens():
#     x = [1,2,3,4,5,6,7,8]
#     n = 0
#     if (x % 2 == 0):
#         n = n.append(x)
#         s = sum(n)
#         print(s)

# evens()

def get_age():
    x = int(input("What is your age?: "))
    if x > 50:
        print("You are old")
    else:
        print("You are young")

get_age()

def age():
    year = 2021
    a = int(input("Please enter your birth year: "))
    y = year - a
    print("Your age is ",y)

age()

def leap_year():
    year = int(input("Please enter your birth year: "))
    if year % 4 == 0:
        print("You were born in a leap year")
    else:
        print("You were not born in a leap year")
leap_year()      

