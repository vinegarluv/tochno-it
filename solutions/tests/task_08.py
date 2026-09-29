from datetime import date
current_year=date.today().year
a=input()
b=int(input())
def century_message(m,n,k):
    l=100-n+k
    return f'{m}, тебе исполнится 100 лет в {l} году'
print(century_message(a,b,current_year))