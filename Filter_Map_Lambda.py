numbers = [1,56,234,87,4,76,24,69,90,135]
def is_even(number): return number % 2 == 0
result = filter(is_even, numbers)
print(*result)
    
answer = filter((lambda number: number % 2 == 0), numbers)
print(*answer)

odd = filter((lambda number: number % 2 == 1), numbers)
print(*odd)

def is_even(numbers):
    return [a for a in numbers if not a % 2 == 0]
print(is_even(numbers))


