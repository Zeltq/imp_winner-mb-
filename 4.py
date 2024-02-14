import csv

A = [x for x in open(r'game.txt')] #Читаем все содержимое в список
F = []
for el in A: #Делим каждый список на элементы и записываем в F
    F.append([x.replace('\n', '') for x in el.split('$')])


#Создаем хэш таблцу для кол-ва багов в игре
my_dict = {}

for el in F:
    if el[0] in my_dict:
        my_dict[el[0]] += 1
    else:
        my_dict[el[0]] = 1

for i in range(1,len(F)): #Каждой игре добавляем ее кол-во багов
    F[i].append(my_dict[F[i][0]])

#Добавляем в первую строку имя и сразу удаляем строку, чтобы можно было отсортировать
F[0].append('counter')
temporary = F[0]
F.pop(0)

#Сортируем по кол-ву багов
F.sort(key=lambda x: x[4])


with open('game_counter.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.writer(file, delimiter='$')
    w.writerow(temporary)
    w.writerows(F)
