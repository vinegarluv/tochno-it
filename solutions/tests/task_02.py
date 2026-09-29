k=float(input())
print('bytes_to_kilobytes or kilobytes_to_bytes')
l=input()
def bytes_to_kilobytes(value):
    return n*1024
def kilobytes_to_bytes(value):
    return n//1024
if l=='bytes to kilobytes':
    print(bytes_to_kilobytes(k))
elif l=='kilobytes to bytes':
    print(kilobytes_to_bytes(k))
else:
    print('ERROR unidentified function')
