
def guests_by_seat(n):
    k=len(n)
    h=[0]*k
    for i in range(k):
        guest=i+1
        seat=n[i]-1
        h[seat]=guest
    return h
print(guests_by_seat([1,2,3,5,4]))