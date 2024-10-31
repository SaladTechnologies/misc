import time

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    while len(fib) < n:
        time.sleep(1)
        print("I am working hard")
        fib.append(fib[-1] + fib[-2])
    
    return fib
