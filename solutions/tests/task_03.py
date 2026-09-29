a,b=map(int,input().split())
def is_divisor(n,m):
    if n==0:
        return False
    if m%n==0:
        return True
    else:
        return False
print(is_divisor(a,b))