def days_in_month(a,b):
    if a==1:
        return 31
    if a==2 and (b%4==0 or b%400==0):
        return 29
    elif a==2 and b%4!=0 or b%100==0:
        return 28
    if a==3:
        return 31
    if a==4:
        return 30
    if a==5:
        return 31
    if a==6:
        return 30
    if a==7:
        return 31
    if a==8:
        return 31
    if a==9:
        return 30
    if a==10:
        return 31
    if a==11:
        return 30
    if a==12:
        return 31
print(days_in_month(11,2025))