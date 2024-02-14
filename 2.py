import csv

A = [x for x in open(r'game.txt')] #Читаем все содержимое в список
F = []
for el in A: #Делим каждый список на элементы и записываем в F
    F.append([x.replace('\n', '') for x in el.split('$')])



#Быстрая сортировка по первому элементу каждого списка, внутри F, вроде бы все элементарно)

def quick_sort(F, first, last):
    if first < last:
        p = partition(F, first, last)
        quick_sort(F, first, p - 1)
        quick_sort(F, p + 1, last)

def partition(F, first, last):
    pivot = F[last][0]
    i = first - 1
    for j in range(first, last):
        if F[j][0] <= pivot:
            i += 1
            F[i], F[j] = F[j], F[i]
    F[i + 1], F[last] = F[last], F[i + 1]
    return i + 1

quick_sort(F, 0, len(F) - 1) #Вызываем функцию, чтобы отсортировать

my_dict = {} #Создаем хэш таблицу, где ключ - название игры, а значение - кол-во багов в этой игре

for el in F:
    if el[0] in my_dict:
        my_dict[el[0]] += 1
    else:
        my_dict[el[0]] = 1

#print(my_dict)
#Далее просто проходимся по каждому ключу - значению, и выводим их в консоль
for key, value in my_dict.items():
    print(f'{key} - количество багов: {value}')


    