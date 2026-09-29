f=[9,2,4,7,9]
def index_of_min(n):
    if not n:
        return -1
    minv=n[0]
    mini=0
    for i in range(1,len(n)):
        if n[i]<minv:
            minv=n[i]
            mini=i
        return mini
print(index_of_min(f))