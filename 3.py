import csv

A = [x for x in open(r'game.txt')] #Читаем все содержимое в список
F = []
for el in A: #Делим каждый список на элементы и записываем в F
    F.append([x.replace('\n', '') for x in el.split('$')])

F.pop(0) #Удаляем заголовок файла, он нам не нужен
F.sort(key=lambda x: x[0]) #Сортируем по имени игры

print(F)

name = input()
#Принимаем имя

#Просто находим в списке нужные элементы и выводим
while name != 'game':
    counter = 0
    flag = 0
    for el in F:
        if name in el[1]:
            counter += 1
            if flag == 0:
                print(f'Персонаж {name} встречается в играх:')
                flag = 1
            if counter <= 5:
                print(el[0])
            else:
                print('И др.')
                break
    if counter == 0:
        print('Этого персонажа не существует')
    name = input()
            
