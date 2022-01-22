# Задание 27 № 27889
# Имеется набор данных, состоящий из пар положительных целых чисел. 
# Необходимо выбрать из каждой пары ровно одно число так, 
# Чтобы сумма всех выбранных чисел не делилась на 3 и при этом была максимально возможной.


from re import S


file = open('27-A_demo.txt', 'r')
b = int(file.readline())
summa = 0
minofpair = []

for i in range(b):
    a = file.readline()
    a = a.split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    summa += int(max(a))
    minofpair.append(int(abs(a[0]-a[1])))

minofpair.sort()
print(minofpair)

for i in range(len(minofpair)):
    if (summa % 3) != 0:
        #print(summa)
        break
    elif ((summa-minofpair[i]) % 3 != 0):
        #print(summa-minofpair[i])
        break

file.close()
