# while
# for
# lambda fx
# functions

# int 
# float
# bool

# ITERABLES - потому, что их можно прогнать через цикл for

# str
# list
# tuple
# dict
# set

# for symbol in 'Hello':
#     print(symbol)

# for letter in 'Hello':
#     print(letter)

# for character in 'Hello':
#     print(character)

# for number in [10, 20, 30]:
#     print(number)

# for text in ['Elbek', 'Hello', 'Python']:
#     print(text)

# for word in ['Elbek', 'Hello', 'Python']:
#     print(word)

# for name in ['Elbek', 'Timur', 'Aziz']:
#     print(name)

# names = ['Elbek']
# names.append("""Zafar
# is the
# best 
# student""")

# "Zafar\nis the\nbest\nstudent"

# names.insert(-1, 'Otabek')
# names.insert(len(names), 'Otabek')

# names.extend(range(10))
# names.extend([1, 2, 3])
# names.extend({1, 2, 3, 3})
# names.extend({"name": "elbek"})





# del names[0]
# names.pop() # удаляет последний элемент
# names.pop(0) # удаляет по индексу
# names.remove('Elbek') # удаляет по значению
# names.clear() # удаляет все из списка


# names_copy = names.copy() # копирует массив
# names.count('Otabek') # считает сколько раз элемент повторяется в списке
# names.index('Elbek') # возвращает индекс элемента

# создает новый перевернутый список
# names[::-1]

# создает новый перевернутый список и переприсваивает в names
# names = names[::-1]

# переворачивает список
# names.reverse()

# обновление списка (замена значения по индексу)
# names[0] = 'Aziz'



# CRUD операции - Create Read Update Delete
# print(names[0])

# На вопрос в чем отличие списка от кортежа следует отвечать:
# 1. Списки изменяемые (мутируемые, модифицируемые)
# 2. Кортежи неизменияемые (немутируемые, немодифицируемые)
# Можно ответить, что списки поддерживают CRUD операции, а кортеж только Read операцию



# names2 = ('Elbek', 'Aziz')

# Спископодобный словарь
# dict = {
#     0: 'Elbek', 
#     1: 'Otabek', 
#     "name": 'Aziz', 
#     2: 'Otabek'
# }

# print(dict[2]) # тут будет ошибка (т.к. несуществующий ключ)
# print(dict.get(2)) # тут будет None

# СО СЛОВАРЯМИ ЖЕЛАТЕЛЬНО ИСПОЛЬЗОВАТЬ get

# dict.pop('name')

# print(dict.keys())
# print(dict.values())

# print(dict)
# print(dict.popitem())
# print(dict.popitem())
# print(dict)

# print(dict.items())
# print(range(1, 10).index(9))

str = 'elbek is 22 years old'

# str = str.replace('is', 'IS')
print(str.find('y'))
# print(str.split(' '))
# print(str.index('d'))
# print(str.strip())
# print(str.rstrip())
# print(str.lstrip())
# print(str.capitalize())
# print(str.lower())
# print(str.upper())
# print('CASEFOLD', str.casefold())
# print('COUNT', str.count('e'))
# print('Ends With', str.endswith('d'))
# print('Swap case', str.swapcase())
# print('abc2'.isalpha())
# print('hello i am elbek'.title())

# ''.encode







# print(str)

# unicode string
# string = 'pythön!'

# # print string
# print('The string is:', string)

# # default encoding to utf-8
# string_utf = string.encode()

# # print result
# print('The encoded version is:', string_utf)


# def format_tel(tel):
#     return f'{tel[0:4]}({tel[4:6]}) {tel[6:9]}-{tel[9:11]}-{tel[11:13]}'

# def format_tel_2(tel):
#     return '{}{}{}{}({}{}) {}{}{}-{}{}-{}{}'.format(*list(tel))

# print(format_tel_2('+998997776655')) # +998(99) 777-66-55
# # Решение с использованием срезов

# print(*list('+998997776655'))
    