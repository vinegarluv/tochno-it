k=float(input())
print('bytes_to_kilobytes or kilobytes_to_bytes')
l=input()
def bytes_to_kilobytes(value):
    return value*1024
def kilobytes_to_bytes(value):
    return value//1024
if l=='bytes_to_kilobytes':
    print(bytes_to_kilobytes(k))
elif l=='kilobytes_to_bytes':
    print(kilobytes_to_bytes(k))
else:
    print('ERROR unidentified function')
