##
# В текстовом файле записан набор натуральных чисел, не превышающих 10^8.
# Гарантируется, что все числа различны. Из набора нужно выбрать три числа, сумма которых делится на 3.
# Какую наибольшую сумму можно при этом получить?
#
# Первая строка входного файла содержит целое число N — общее количество чисел в наборе.
# Каждая из следующих N строк содержит одно число.
## 
file = open('27-B.txt', 'r')
a = []
len = int(file.readline())
for i in range(len):
    a.append(int(file.readline()))

a.sort(reverse = True)

b = []
for k in range(0,len):
    for j in range(k+1,len-1):
        for i in range(j+1,len-2):
            if (a[k]+a[j]+a[i]) % 3 == 0:
                b.append(a[k] + a[j] + a[i])
                #print(a[k]+a[j]+a[i]," (", k,",", j, ",", i, ")")
                break
        if j>1000:
            break
b.sort(reverse=True)
print(b[0])

file.close()
