import math
print ("Vvedite chislo:")
while True:
    try:
        a = int(input())
        if a == str or a == float or a <2:
            raise ValueError
        break    
    except ValueError:
        print("Nekkorektny vvod")
        quit()
if a == 2: 
    print ("Chislo prostoe")
    quit()
i = 2 #крч, переменная(делитель), увеличиваем до лимита (перебираем делители от 2 до sqrt(a))
limit = int(math.sqrt(a))
b = True
while i <= limit:
    if a % i == 0:
        b = False 
        #print("Chislo ne prostoe")
        quit()    
    i += 1   
if b == True:
    print ("Chislo prostoe")
else:   
    print ("Chislo Sostavnoe")
