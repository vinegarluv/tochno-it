a,b=map(int,input().split())
def swap(n,m):
    return n-n+m,m-m+n
print(swap(a,b))