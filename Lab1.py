# import math 


# print("hello")
# #print(hello)  #error since hello is not defined

# #Maths
# print(4+5)
# print(8*3)
# print(4/3)

# #Strings
# print("abc" + "def")
# print("123" + "5")

# #Variables
# first = "hello"
# second = " world"
# type(first)
# print(first + second)

# #User input 
# name = input("What is your name?: ")
# type(name)
# age = input("What is your age?: ")
# type(age)

# #To try
# radian = (32*math.pi)/180
# print(radian)

# radius = int(input("Please enter your radius: "))
# area = math.pi*radius**2
# print(area)
# volume = (4/3)*math.pi*radius**3
# print(volume)

# time = "Have a great afternoon. Hope it is bright and shiny today"
# print(time)

# x = "I have to split this sentence"
# sentence = x.split(" ")
# print(sentence)

# join = "I want a pet"
# join_sentence = " rabbit"
# print(join + join_sentence)

# print ("I have to go" + " to" + " the" + " market")


def odd_or_even():
    number = int(input("Enter your number: "))
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
odd_or_even()