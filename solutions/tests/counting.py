a=int(input())
def factorial(n):
    o=1
    if n>0:
        for i in range(n,0,-1):
            o*=i
        return o
    if n==0:
        return 1
    if n<0:
        return None
print(factorial(a))
b,c=map(int,input().split())
def arrangements(n,k):
    l=factorial(n)/factorial(n-k)
    return l
print(arrangements(b,c))