a,b=map(float,input().split())
def shortest_distance(kilometers,meters):
    l=kilometers*1000
    return min(l,meters)
print(shortest_distance(a,b))
