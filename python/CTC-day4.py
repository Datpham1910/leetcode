def fibo(n):
    arr = [None for _ in range(n)]
    arr[0] = 1
    arr[1] = 2
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i -2 ]
    return arr[-1]

def fibo_n(n):
    if n == 1: return 1
    if n == 2: return 2
    return fibo_n(n - 1) + fibo_n(n - 2)

print(fibo(50))