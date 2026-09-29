a,b=map(int,input().split())
def compare(m,n):
    if m>n:
        return 'Number m > n'
    if m<n:
        return 'Number m < n'
    if m==n:
        return 'The numbers are equal'
print(compare(a,b))