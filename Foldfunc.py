from functools import reduce


total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
print(total)

words = ["hello","world", "hi"]
def join_string(words):
    s = reduce((lambda x, y: x + " " + y), words) #this reduces the sentence by joining them together
    print(s)
join_string(words)

