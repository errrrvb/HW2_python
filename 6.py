n = int(input()) # ввод числа
a = 1 # счет чисел для цикла for
b = 1 # запись чисел в ответ
for i in range(n): # цикл, состоящий из n действий
    c = 1/a # переменная, используемая для добавления чисел к переменной b
    b += c # прибавляем к b
    a+=1 # увеличиваем на 1 для продолжения цикла
print(round(b, 5)) # округление до 5 знаков
