# import random

# all_choices = [i for i in range(10)]
# while True:
#
#     random_choice = random.choice(all_choices)
#     if random_choice % 3 == 0:
#         break
#
#     print(f'Selected choice was {random_choice}')
# print(f'Exit choice was {random_choice}')
#
#
# for i in all_choices:
#     if i % 2 != 0:
#         continue
#     print(f'Numar par {i}')
#
#
# if True:
#     pass
# else:
#     print('this is false')

# def my_function(list_param):
#     list_param = list(list_param)
#     list_param.append(4)
#
#
# my_list = [1, 2, 3]
# my_function(my_list)
# print(my_list)


# def my_function(nume, prenume, varsta=18, inaltime=180):
#     print(f'Nume: {nume}, Prenume:{prenume}, Varsta: {varsta}, Inaltime :{inaltime}')
#
#
# nume = 'Andrei'
# prenume = 'Razvan'
#
# my_function(nume, prenume, varsta=22, inaltime=170)


# def my_function(param_1, param_2, *args, name, age, **kwargs):
#     print('param1: ', param_1)
#     print('param2: ', param_2)
#     for p in args:
#         print(p)
#     print('name: ', name)
#     print('age: ', age)
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k, '->', v)
#
#
# my_function(1, 2, 3, 4, 5, 'some_string', name='Razvan', age=36, job='developer', city='Bucuresti')

# my_var = input('introduceti un nr: ')
#
# try:
#     my_int = int(my_var)
#     print(my_int)
# except ValueError as e:
#     print('Va rugam sa introduceti un int! Urmatoarea eroare s-a produs: ', e)
# except NameError as e:
#     print('Ati folosit o variabila nedeclarata in cod: ', e)
#
# else:
#     print('We are here because no exception was fired!')
# finally:
#     print('We execute this block no matter what!')

# print(dir(__builtins__))



# def my_function():
#
#     msg = 'Salut'
#     print(msg)
#
#
# my_function()
# print(msg)


def my_function():
    def my_second_function():
        msg = 'lolo'
        print(f'my_second-function: {msg}')

    msg = "Hello World!"
    my_second_function()
    print(f'my_function: {msg}')


my_function()













