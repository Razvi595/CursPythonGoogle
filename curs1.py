from decimal import Decimal
print("Hello world")
price = Decimal(49)
name = 'Razvan'
# print(f'For only {price:.2f} dollars {name} have a nice day')
# print(name)

#strings are immutable

names = ['Ana', 'Ioana', 'Maria', 'Alexandra', 'Daniela']
print(names)
names[0] = 'Elena'
print(names)
#names.sort()
print(sorted(names))
print(names)

names = ['Ana', 'Ana', 'Ioana', 'Maria', 'Alexandra', 'Daniela', 'Ioana']
print(names)
set_names = set(names)
print(set_names)

new_names = ['Ana', 'Ioana']
set_new_names = set(new_names)
print(set_new_names.issubset(set_names))

new_list = list(set_new_names)
print(new_list)

# unique_list = []
# for name in names:
#     if name not in unique_list:
#         unique_list.append(name)
# print(names)
# print(unique_list)

print(list(set(names)))


all_words = {
    'vacanta': ['www.tui.ro', 'www.booking.com'],
    'grecia' : ['www.wikipedia.com', 'www.booking.com']
}

person = {
    'name': 'Ion',
    'last_name': 'Popescu',
    'age': 34,
}

person2 = {
    'name': 'Ion',
    'last_name': 'Popescu'

}

print(person['age'])
print(person2.get('age', 0))

days_of_the_week = ('Mon', 'Tue', 'Wed')


# declararea listei
lst = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișarea listei sortate ascendent (fara a modifica lista inițială)
print(sorted(lst))

# afișarea listei sortate descendent (fara a modifica lista inițială)
print(sorted(lst, reverse=True))

# afișarea numerelor cu indici pari din listă (folosind DOAR slice)
print(lst[::2])

# afișarea numerelor cu indici impari din listă (folosind DOAR slice)
print(lst[1::2])

# afișarea elementelor multipli ai lui 3
print([x for x in lst if x % 3 == 0])
