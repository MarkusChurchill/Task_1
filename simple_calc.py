yournumber = float(input("Введите число: "))
operator=[0]
while operator[0] != '=':
    operator1 = input()
    operator2 = [operator1]
    print(str.replace, "operator1")
    print(operator2, "operator2")
    operator = list(operator1)
    print(operator, 'operator')
    print(len(operator))

    # проверка на выход
    if operator[0] == '=':
        break
    print('Проверка на количество элементов')
    if len(operator)==2:
        a=operator[1]
    else:
        print('Ввел ли я с пробелом?')
        #Проверка на ввод с пробелом
        if operator[1] == ' ' or operator[2] == ' ':
            print('Вы ввели с пробелом')
            if operator[1] == '/' or operator[1] == '*':
                operator[0] = operator[0] + operator[1]
                del operator[1]
                print(operator, 'Удален оператор / или *')
            #Проверка на цифру и число
            if len(operator) == 3: #Если формат записи "+ 9"
                a=operator[2]
            else:
                #Формирование списка в число с пробелом
                i = 4
                a = operator[2] + operator[3]
                for i in range(4, int(len(operator))):
                    a = a + operator[i]
                    a = int(a)
                    print(a)

        # Если вбивать без пробела
        else:
            print('Вы ввели без пробела')
            # Проверка на двойные * или /
            if operator[1] == '/' or operator[1] == '*':
                operator[0] = operator[0] + operator[1]
                del operator[1]
                print(operator, 'Удален оператор / или *')

            print('Формирование списка в число')
            if len(operator)== 2:
                a=operator[1]
            else:
                i = 3
                a = operator[1] + operator[2]
                for i in range(3, int(len(operator))):
                    a = a + operator[i]
                    a=int(a)
                    print(a)

    #мат операции
    if operator[0] == '+':
        yournumber = yournumber + int(a)
        print(yournumber)
    elif operator[0] == '-':
        yournumber = yournumber - int(a)
        print(yournumber)
    elif operator[0] == '*':
        yournumber = yournumber * int(a)
        print(yournumber)
    elif operator[0] == '/':
        yournumber = yournumber / int(a)
        print(yournumber)
    elif operator[0] == '//':
        yournumber = yournumber // int(a)
        print(yournumber)
    elif operator[0] == '%':
        yournumber = yournumber % int(a)
        print(yournumber)
    elif operator[0] == '':
        yournumber = yournumber  int(a)
        print(yournumber)
    else:
        print("Не корректный ввод.")
        quit()
print('Ваше число: ', yournumber)
