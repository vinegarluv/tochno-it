a,b=map(int,input().split())
def is_divisor(a,b):
    if a==0:
        return False
    if b%a==0:
        return True
    else:
        return False
print(is_divisor(a,b))
