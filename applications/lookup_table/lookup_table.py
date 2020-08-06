# Your code here
import math
import random

power_cache = {}

for x in range(2,14):
    for y in range(3, 6):
        if x not in power_cache.keys():
            power_cache[x] = {}
        power_cache[x][y] = math.pow(x, y)

factorial_cache = {}

def factorial(n):
    if n not in factorial_cache:
        factorial_cache[n] = math.factorial(n)
    return factorial_cache[n]

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    v = power_cache[x][y]
    v = factorial(v)
    v //= (x + y)
    v %= 982451653
    
    return v

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
