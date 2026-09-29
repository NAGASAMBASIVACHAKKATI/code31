def num(n):
    if n==0:
        return 1
    return n*num(n-1)
print(num(5))
