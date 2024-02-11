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

# task 3
import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    '''Parse a log line and return a dictionary with parsed components.'''
    components = line.strip().split()
    if len(components) < 6:
        print(f'Invalid log line: {line}')
        return None  # Skip invalid log lines
    return {
        'datetime': components[0] + ' ' + components[1],
        'level': components[2],
        'message': ' '.join(components[5:])  # Concatenate remaining components as message
    }


def load_logs(file_path: str) -> list:
    '''Load logs from a file.'''
    logs = []
    try:
        with open(file_path, 'r') as fh:
            for line in fh:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print('File not found.')
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    '''Filter logs by level.'''
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    '''Count logs by level.'''
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    '''Display log counts in a table.'''
    print('   Level of log   | Amount')
    print('------------------|------')
    for level, count in counts.items():
        print(f'{level:<17} | {count:<9}')

def main():
    if len(sys.argv) < 2:
        print('Usage: python main.py <log_file_path> [<logs.level>]')
        return
    
    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)

    if len(sys.argv) == 3:
        log_level = sys.argv[2].upper()
        logs = filter_logs_by_level(logs, log_level)
        print(f"Log details for level '{log_level}':")
        for log in logs:
            if log:  # Check if log is not None
                print(f"{log['datetime']} - {log['message']}")
                print()

    log_counts = count_logs_by_level([log for log in logs if log])  # Filter out None values
    display_log_counts(log_counts)

if __name__ == '__main__':
    main()




