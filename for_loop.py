for i in range(1,11):
    print(i)
# i is a list of integers from 1 to 10

for j in [1,2,3]:
    print(j)

for j in range(1,4):
    print(j)

for m in range(0,19):
    if m % 2 == 0:
        print(m)

#this function prints a pattern of squares using asterix
def pattern():
    for i in range(1,5):
        for j in range(1,5):
            print("*",end="")
        print()
    
pattern()

def arrow():
    for i in range(5):
        print(i*"*")
    for i in [3,2,1]:
        print(i*"*")

arrow()

def condition():
    s = input("Please enter your sentence: ")
    l = s.find("k") 
    if l == -1:
        print(False)
    else:
        print(True)

condition()

def c():
    def conditional():
        s = input("Please enter your sentence: ")
        l = s.find("s") 
        m = s.find("m")
        if l  == -1:
            print(False)
        elif m == -1:
            print(False)
        else:
             print(True)
    conditional()
c()