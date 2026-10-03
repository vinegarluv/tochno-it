a,b=map(int, input().split())
def month_calendar(start_weekday, days):
    f=[]
    l=[]
    for i in range(0,start_weekday):
        f.append(' ')
    for i in range(1,days+1):
        f.append(f'{i:2}')
        if len(f)==7:
            l.append(' '.join(f))
            f=[]
    return '\n'.join(l)
print(month_calendar(a,b))