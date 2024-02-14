import csv

#В начало строки я специаьно добавил символ, которого нет в названии игр, чтобы отсчет был с единицы, а не с нуля
alph = '_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM:,0123456789\'-. '

def get_hash(s_1,s_2):
    '''
    В функцию поступаем название игры и имя персонажа, далее генерируем хэш, ничего сложного
    '''
    s = s_1 + s_2
    hash_value = 0
    p = 65
    m = 10**9+9
    for i in range(len(s)):
        hash_value += alph.index(s[i])*p**i
    return hash_value % m

A = [x for x in open(r'game.txt')] #Читаем все содержимое в список
F = []
for el in A: #Делим каждый список на элементы и записываем в F
    F.append([x.replace('\n', '') for x in el.split('$')])

#Здесь просто проходим по всему F и удобно добавляет хэш в начало листа
for i in range(1,len(F)):
    hash = get_hash(F[i][0], F[i][1])
    F[i].reverse()
    F[i].append(hash)
    F[i].reverse()


F[0] = ['Hash','GameName', 'characters', 'nameError','date','counter']
#Остается записать все в csv файл
with open('game_with_hash.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.writer(file, delimiter='$')
    w.writerows(F)
   
