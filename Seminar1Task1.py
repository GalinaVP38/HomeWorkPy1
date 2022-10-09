print("Введите день недели: ")
dayNum = int(input())
if dayNum==6 or dayNum==7:
    print("Выходной")
elif dayNum==1 or dayNum==2 or dayNum==3 or dayNum==4 or dayNum==5:
    print("Будний день")
else:
    print("Число не обозначает день недели")
