def fibonacci_sequence(n):
    fn = [0, 1]
    while len(fn) < n:
        next_num = fn[-1]+ fn[-2]
        fn.append(next_num)
    return fn
print(fibonacci_sequence(6))