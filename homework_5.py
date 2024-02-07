# task 1
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))

# task 2
import re
from typing import Callable

def generator_numbers(text: str):
    words = text.split()
    float_pattern = r'\b\d+\.\d+\b'
    for word in words:
        numbers = re.findall(float_pattern, word)
        for number in numbers:
            yield float(number)

def sum_profit(text: str, func: Callable) -> float:
    total = 0
    for number in func(text):
        total += number 
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")




