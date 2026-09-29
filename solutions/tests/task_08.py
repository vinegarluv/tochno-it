from datetime import date
current_year=date.today().year
a=input()
b=int(input())
def century_message(name,age,current_year):
    l=100-age+current_year
    return f'{m}, тебе исполнится 100 лет в {l} году'
print(century_message(a,b,current_year))
