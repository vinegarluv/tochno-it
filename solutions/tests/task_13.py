n=int(input())
def multiplication_table(n):
    i=0
    while i != 9:
        i+=1
        k=n*i
        print(f'{n} x {i} = {k}')
    i+=1
    k=n*i
    return f'{n} x {i} = {k}'
print(multiplication_table(n))