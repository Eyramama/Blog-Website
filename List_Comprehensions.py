# words = ["hello","world", "hi"]
# [len(word) for word in words]
# [len(word) for word in words if word != "the"]

# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# def positive_numbers(num): return [x for x in numbers if x > 0]
# print(positive_numbers(numbers))

# number = [12, 54, 33, 67, 24, 89, 11, 24, 47]
# def even_numbers(num): return [x for x in number if x % 2 == 0]
# print(even_numbers(number))

words = ["hello", "my", "name", "is", "Sam"]
def tuples(word):
    h = [len(a) for a in word]
    j = [a.upper() for a in word]
    return list (map(lambda x, y: (x,y), j,h))
print(tuples(words))





