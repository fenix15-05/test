import random

count = int(input())
file = open('a.txt', 'w')
file.write(str(count)+str("\n"))
for i in range(0,count):
    file.write(str(random.randint(0, 9)) + str(" "))
    file.write(str(random.randint(-5555, 55555)) + str('\n'))
file.close()




