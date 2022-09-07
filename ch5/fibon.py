def fibonacci_list(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.extend([a, b])
        a, b = b, a + b
    
    return result

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b
    
def fibonacci_functional():
    a, b = 0, 1
    calls = 0
    def inner():
        nonlocal a
        nonlocal b
        nonlocal calls
        calls += 1
        if calls == 1:
            return a
        if calls == 2:
            return b
        a, b = b, a + b

        return b
    
    return inner

def fibonacci_recursive(n):
    def rec(a, b, calls, limit):
        a, b = b, a + b
        if calls == limit:
            return b
        return rec(a, b, calls+1, limit)
    
    return rec(0, 1, 0, n)

        
        

        



