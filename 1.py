import csv

A = [x for x in open(r'game.txt')] #Читаем все содержимое в список
F = []
for el in A: #Делим каждый список на элементы и записываем в F
    F.append([x.replace('\n', '') for x in el.split('$')])

#Ищем ошибки, содержащие 55 и меняем, как указано в тз + выводим для отчета
for el in F:
    if '55' in el[2]:
        print(f'У персонажа:\t{el[1]}\tв игре\t{el[0]}\tнашлась ошибка с кодом:\t {el[2]}.\tДата фиксации:\t {el[3]}')
        el[2] = 'Done'
        el[3] = '0000-00-00'


#Записываем все в csv файл  

with open('game_new.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.writer(file, delimiter='$')
    w.writerows(F)
