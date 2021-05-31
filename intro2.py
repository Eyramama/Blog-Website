names = ["Eyram","Stephanie","Sam","Henry"]

# #  for name in names:
# #      len(names)
     

# upper = map(len, names)
# print(*upper)

# lengths = [3,5,6,9]
# def sqr(x): return x ** 2

# squares = map(sqr, lengths)
# print(*squares)

# def sqr(x): return len(x)**2
# sqrlengths = map(sqr, names)
# sqrlens = map(sqr, sqrlengths)
# print(*sqrlengths)
# print(*sqrlens)

# lambda is a function without a name
# sqrlengths = map(len, names)
# sqrlens = map((lambda x: x** 2), sqrlengths)
# sqrlens = map((lambda x: x** 3), sqrlengths)
# print(*sqrlens)

ages = [16,17,18,19,20]
def can_vote(x): return x >= 18
voters = filter(can_vote, ages)
print(*voters)
