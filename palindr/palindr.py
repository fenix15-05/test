def palindr(slovo):
    for i in range(0,len(slovo)//2):
        if slovo[i] != slovo[(len(slovo)-1)-i]:
            return False
    print(slovo)
    return True
vvod = str(input())
str_start = 0
str_end = 0
vvod += " "
counter = 0
for i in range(0,len(vvod)):
    if vvod[i] == " ":
        str_end = i
        slovo = (vvod[str_start:str_end])
        if str_end - str_start >= 1:
            if (palindr(slovo)):
                counter +=1
        str_start = str_end + 1
print ("палиндромов",counter)


