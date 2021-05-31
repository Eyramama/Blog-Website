# i = 6
# while(i < 19):
#     i = i + 1
#     print(i)

# j = 12
# if j % 2 == 0:
#     while(j < 18):
#         j = j + 2
#         print(j)
# else:
#     print("none")


# def evens(x, y):
#     if x % 2 == 0:
#         while(x < y):
#             x = x + 2
#             print(x)
#     else:
#         print("none")

# evens(2, 18)

def reverse_evens(x, y):
    i = y-1
    while (i < y):
        if(i % 2 == 0):
            print(i)
        i = i + 1

reverse_evens(2, 12)


