print('input value:')
k=float(input())
print('bytes to kilobytes or kilobytes to bytes')
l=input()
def bytes_to_kilobytes(n):
    return n*1024
def kilobytes_to_bytes(n):
    return n/1024
if l=='bytes to kilobytes':
    print(bytes_to_kilobytes(k))
elif l=='kilobytes to bytes':
    print(kilobytes_to_bytes(k))
else:
    print('ERROR unidentified function')