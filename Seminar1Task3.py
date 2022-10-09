print("Введите значение координаты Х: ")
x=float(input())
print("Введите значение координаты Y: ")
y=float(input())
if x==0 or y==0:
    print("Введите координаты отличные от нуля")
if x>0 and y>0:
    print("1 четверть")
if x<0 and y>0:
    print("4 четверть")
if x>0 and y<0:
    print("2 четверть")
if x<0 and y<0:
    print("3 четверть")
