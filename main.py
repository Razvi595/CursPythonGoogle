 #print("i love pizza")
 #print("it's really good")

     #4 tipuri de date in python

# first_name = "Razvan"
# last_name = "Andrei"
# full_name = first_name + " " + last_name
# print("hello " + full_name)
# print(type(name))

# age = 22
# age = age + 1 # age +=1
# print("your age is " + str(age)) #str(  ) transforma int ul in string
# #print(type(age))


# height = 22.5
# print("your height is " + str(height) + "cm")
# #print(type(height))


# human = True
# print("Are u a human : " + str(human))
# # print(type(human))

     #Multiple assignment

# name = "Razvan"
# age = 21
# attractive = True

# name, age, attractive = "Razvan", 21, True
#
# print(name)
# print(age)
# print(attractive)
#
# spongebob = 30
# patrick = 30
# sandy = 30
# squidward = 30
#
# spongebob = patrick = sandy = squidward = 30



    # string methods

# name = "Razvan"
# print(len(name)) # lungimea
# print(name.find("R")) # pe ce pozitie este caracterul respectiv
# print(name.capitalize()) #pune litera mare la inceput
# print(name.upper()) # litere mari
# print(name.lower()) # litere mici
# print(name.isdigit()) # este numar?
# print(name.isalpha()) #este format din caractere alfabetice?
# print(name.count("a")) #numara cate litere a sunt
# print(name.replace("a", "o")) #inlocuieste a cu o
# print(name*3)


    # Type casting = convertirea tipul de data al unei variabile intr-un alt tip de data

# x = 1 #int
# y = 2.0 #float
# z = "3" #str
#
# x = str(x) #/float/int
# y = str(y)
# z = str(z)
#
# print("X is " +str(x))
# print("Y is " +str(y))
# print("Z is " +z)


    # User input

# name = input("What is your name ?: ") # default input este string
# age = int(input("How old are you ?: ")) # trebuie sa fie int ca sa poti face operatii matematice
# height = float(input("How tall are you? :"))
#
#
# print("Hello " + name)
# print("you are " + str(age) + " years old") # il readucem la tipul string ca sa putem face string concatenation
# print("You are " + str(height) + " cm tall")


    # Math functions
# import math
# pi = 3.14
# x = 1
# y = 2
# z = 3
# print(round(pi))
# print(math.ceil(pi)) # aproximeaza in sus
# print(math.floor(pi)) # aproximeaza in jos
# print(abs(pi)) #modul
# print(pow(pi,2)) # ridica la putere
# print(math.sqrt(pi))
# print(max(x,y,z,pi))
# print(min(x,y,z,pi))


   # String slicing - creating a substring by extracting element from another string
   # indexing[] sau slice()
   # [start:stop:step]

# name = "Razvan Andrei"
# first_name = name[:6]   #PRIMUL INDEX ESTE INCLUS, ULTIMUL INDEX ESTE EXCLUS
# last_name = name[7:] #sau [7:13]
# funky_name = name[0:13:2] #sau [::2]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])



    # If statements

# age = int(input("How old are you?: "))  # conteaza ordinea elif urilor
#
# if age >= 18:
#     print("You are an adult!")
# elif age == 100:
#     printf("You are a century old")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")


    # Logical operators  :  and / or / not


# temp = int(input("What is the temperature outside?: "))
# if not(temp >= 0 and temp <= 30):
#     print("The temperature is good today! ")
#     print("Go outside")
# elif not(temp < 0 or temp > 30):
#     print("The temperature is bad today")
#     print("Stay inside!")

    # While loop - unlimited

# name = ""
#
# while len(name) == 0:
#     name = input("Enter your name: ")
# print("Hello " + name)


    # For loop - limited

import time

# for i in range(10):
#     print(i)

# for i in range(50,100,2):  #(inclusive, exclusive)
#     print(i)

# for i in "Razvan Andrei":
#     print(i)

# for seconds in range(10, 0, -1):   # countdown time
#     print(seconds)
#     time.sleep(1)
# print("Happy new year !")



    # Nested loops

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Eneter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")  #end il folosim ca sa nu treaca pe linie noua dupa fiecare print
#     print()  # printeaza o linie noua


    # Loop control statements ( break continue pass )

    # break = uded to terminate the loop entirely
    # continue = skips to the next iteration of the loop
    # pass = does nothing acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break


# phone_number = "123-456-6789"  # scrie numarul fara linii
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")


# for i in range(1,21):  # il exclude pe 13
#     if i == 13:
#         pass
#     else :
#         print(i)


    # Lists = used to store multiple items in a single variable

# food = ["pizza","hamburger","hotdog","spaghetti"]
#
# food[0] = "sushi"
# print(food[0])


# food.append("ice cream")  # adauga la sfarsit
# food.remove("hotdog")
# food.pop()  # scoate ultimul element
# food.insert(0,"cake")
# food.sort() # sorteaza alfabetic
# food.clear()


# for x in food:
#     print(x)



    # 2D Lists  =  a list of lists

# drinks = ["coffe","soda","tea"]
# dinner = ["pizza","hamburger","hotdog"]
# dessert = ["cake","ice cream"]
#
# food = [drinks, dinner, dessert]
# print(food[0][2])



    # Tuple = collection which is ordered and unchangeable ; used to group together related data
    # diferenta intre tupluri si liste e ca tuplurile sunt ordonate si nu le poti schimba

# student = ("Razvan", 22, "male")
# print(student.count("Razvan"))
# print(student.index("male"))
#
# for x in student:
#     print(x)
#
# if "Razvan" in student:
#     print("Razvan is here")


    # Sets = collection which is unordered, unindexed. No duplicate values

# utensiles = {"fork", "spoon", "knife"}
#
# dishes = {"bowl", "plate", "cup", "knife"}

# utensiles.add("napkin")
# utensiles.remove("fork")
# utensiles.clear()
# utensiles.update(dishes)

# dinner_table = utensiles.union(dishes)

# print(utensiles.difference(dishes))  # ce are utensils si dishes nu are
#print(utensiles.intersection(dishes))

# for x in dinner_table:
#     print(x)


    # Dictionaries = a changeable, unordered collection of unique key:value pairs
            # fast because they use hashing, allow us to access a value quickly


# capitals = {'USA':'Washington DC',
#             'India':'New Delhi',
#             'China':'Beijing',
#             'Russia':'Moscow'}
# print(capitals['Germany'])
# print(capitals.get('Germany'))  # daca nu pun get imi da eroare pt ca Germany nu e in dictionar
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())



# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()
#
# for key,value  in capitals.items():
#     print(key,value)



    # Index operator [] - gives access to a sequence's element (str,list,tuple)

# name = "Razvan Andrei!"

# if name[0].islower():
#     name = name.capitalize()


# first_name = name[0:6].upper()
# last_name = name[7:].lower()
# last_character = name[-1]
# print(last_name)
# print(last_character)


    # Functions

# def hello(first_name, last_name, age):  # parametri
#     print("Hello! "+first_name+ " "+ last_name)
#     print("Have a nice day ! You are " + str(age) + " years old")
#
# # hello("Razvan")  #argumet
#
# hello("Razvan", "Andrei",21)


    # Return statement = functions send Python values/objects back to the caller.

# def multiply(number1, number2):
#     result = number1 * number2
#     return result   # sau direct return number1*number2
#
# x = multiply(6,8)
#
# print(multiply(6,8))


    # Keyword arguments = arguments preceded by an identifier when we pass them to a function
    # The order of the arguments doesn't matter, unlike positional arguments
    # Python knows the name of the arguments that our function receives


# def hello(first,middle,last):
#     print("Hello "+first+" "+middle+" "+last)
#
# hello(last="Razvan",middle="Marius",first="Andrei")



    # Nested function calls = function calls inside other function calls

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Enter a whole positive number: ")))))



    # Variable scope = the region that variable is recognized
    # A variable is only available from inside the region it is created
    # A global and locally scoped versions of variable can be created

# name = "Razvan" #global scope (available inside&outside functions)
#
# def display_name():
#     name = "Andrei"   # local variable that has a local scope ( available only inside this function)
#     print(name)
#
#
# display_name()
# print(name)

# LEGB rule
# L = local
# E = Enclosing
# G = Global
# B = Built-in



    # Args = parameter that will pack all arguments into a tuple
        # useful so that a function can accept a varying amount of arguments


# def add(*stuff):  #de obicei este *args
#     sum = 0
#     stuff = list(stuff)
#     stuff[0]=0
#     for i in stuff:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,5))




    # Kwargs = parameter that will pack all arguments into a dictionary = key word argument
    # useful so that a function can accept a varying amount of keyword arguments



# def hello(**kwargs):   # dublu **
#     #print("Hello "+ kwargs['first'] + " " + kwargs['last'])
#     print("hello", end=" ")
#     for key,value in kwargs.items():
#         print(value, end=" ")
#
# hello(title="Mr.",first="Razvan",middle="Dude", last="Andrei")



    # String format = str.format() =  optional method that gives user more control when displaying output


# animal = "cow"
# item = "moon"

#print("the "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format("cow","moon"))
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {0}".format(animal,item)) #inverseaza
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))

# text = " The {} jumped over the {}"
# print(text.format(animal, item))


# name = "Razvan"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name)) #lasa 10 spatii dupa nume
# print("Hello, my name is {:<10}. Nice to meet you".format(name)) # left align
# print("Hello, my name is {:>10}. Nice to meet you".format(name)) # right align
# print("Hello, my name is {:^10}. Nice to meet you".format(name)) # center align


# number = 3.14159
# number1 = 1000
# print("the number pi is {:.2f}".format(number)) # doar 2 zecimale, f de la float
# print("the number pi is {:,}".format(number1)) # adauga , la mii
# print("the number pi is {:b}".format(number1)) #face in binar
# print("the number pi is {:o}".format(number1))
# print("the number pi is {:X}".format(number1)) # in hexa
# print("the number pi is {:E}".format(number1)) # scientific notation



    # Random numbers

# import random
#
# x = random.randint(1,6)
# y = random.random() # nr random intre 0 si 1
#
# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)
#
#
# cards = [1,2,3,4,5,6,7,8,9,"J", "Q", "K", "A"]
# random.shuffle(cards)
# print(cards)


    # Exceptions = events detected during execution that interrupt the flow of a program

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:            # ar fi bine sa stim exact ce exceptii putem avea ca sa instiintam user ul
#     print(e)
#     print("You can't divide by zero! idiot")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers please")
# except Exception as e:
#     print(e) #iti zice eroarea
#     print("Something went wrong")
# else:
#     print(result)
# finally:  #mereu va face asta
#     print("This wil always execute")



    # File detection

# import os
#
# path = "E:\\Desktop\\folder" # dublu \\
#
# if os.path.exists(path):
#     print("that location exists!")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("that is a directory")
# else:
#     print("That location doesn't exist!")



    # Read a file


# try:
#     with open('test.txt') as file:  #functia open inchide automat fisierul dupa ce il foloseste
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found")

# print(file.closed)


    # Write a file


# text = "Have a nice day! See ya\n"
# with open('test.txt','w') as file:  #asa se scrie
#     file.write(text)
# with open('test.txt','a') as file:  #asa se adauga text
#     file.write(text)



    # Copy a file


# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

# import shutil
#
# shutil.copyfile('test.txt', 'E:\\Desktop\\copy.txt') #src, dstn  #daca exista deja fisierul face overwrite



    # Move a file


# import os
# source = "test.txt"  # merge si cu folder ; da eroare daca trebuie sa mute de pe un disk pe altul
# destination = "C:\\Users\\Razvan Andrei\\PycharmProjects\\test.txt"
#
# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source+" was moved")
#
# except FileNotFoundError:
#     print(source+" was not found")


    # Delete a file


# import os
# import shutil
# path = "folder"
#
# try:
#     #os.remove(path)     #sterge fisier, dar nu sterge folder gol
#     #os.rmdir(path)      #sterge folder gol \\remove tree
#     shutil.rmtree(path)  #sterge un folder si toate fisierele din el \\remove tree
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to delete that")
# except OSError:
#     print("You cannot delete that using that function")
# else:
#     print(path+" was deleted")


    # Modules = a file containing python code. May contain functions, classes, etc
        # used with modular programming which is to separate a program into parts

# import messages as msg
#
# msg.hello()
# msg.bye()

#sau


# from messages import hello,bye  #sau import *  le importeaza pe toate
# hello()
# bye()


# help("math")


    # Rock, paper, scissors game


# import random
#
# while True:  # while loop ca sa intrebam player ul daca mai vrea sa se joace
#     choices = ["rock", "paper", "scissors"]
#
#     computer = random.choice(choices)
#     player = None
#
#     while player not in choices:
#         player = input("rock, paper, or scissors?: ").lower()
#
#     if player == computer:
#         print("computer: ", computer)
#         print("player: ", player)
#         print("Tie!")
#     elif player == "rock":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")
#
#     elif player == "scissors":
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")
#     elif player == "paper":
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")
#     play_again = input("Play again? (yes/no): ").lower()
#
#     if play_again != "yes":
#         break
#
# print("Bye!")




    # Quiz game
# -----------------------------
# def new_game():
#
#     guesses = []
#     correct_guesses = 0
#     question_num = 1 #reprez prima intrebare
#
#     for key in questions:
#         print("-----------------------------")
#         print(key)
#         for i in options[question_num-1]:  #afiseaza prima lista din lista de liste
#             print(i)
#         guess = input("Enter (A, B, C, or D): ")
#         guess = guess.upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key), guess)  # get(key) returneaza valoarea cheii (raspunnsul corect la intrebare)
#         question_num += 1
#
#     display_score(correct_guesses, guesses)
# # -----------------------------
# def check_answer(answer, guess):
#     if answer == guess:
#         print("CORRECT!")
#         return 1
#     else:
#         print("WRONG!")
#         return 0
# # -----------------------------
# def display_score(correct_guesses, guesses):
#     print("-----------------------------")
#     print("RESULTS")
#     print("-----------------------------")
#
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()
#
#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()
#
#     score = int((correct_guesses/len(questions))*100)
#     print("Your score is: "+str(score)+"%")
# # -----------------------------
# def play_again():
#     response = input("Do you want to play again? (yes/no): ")
#     response = response.upper()
#
#     if response == "YES":
#         return True
#     else:
#         return False
# # -----------------------------
#
#
# questions = {
#     "Who created Python?: ": "A",
#     "What year was Python created?: ": "B",
#     "Python is tributed to which comedy group?: ": "C",
#     "IS the Earth round?: ": "A"
# }
#
# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
#            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#            ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]
#
# new_game()
#
#
# while play_again():
#     new_game()
#
# print("Byeee!")



    # OOP (object oriented programming) POOP
    # object = instance of a class
    # Object - attributes = is/has (name, age, height)
    #        - methods = actions (eat, sleep, make yt videos)


# from car import Car
#
# car_1 = Car("Chevy", "Corvette", 2021, "blue")
# car_2 = Car("Ford", "Mustang", 2022, "red")
#
#
# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)
#
# car_2.drive()
# car_2.stop()



    # Class variables


# from car import Car
#
# car_1 = Car("Chevy", "Corvette", 2021, "blue")
# car_2 = Car("Ford", "Mustang", 2022, "red")
#
# Car.wheels = 2
# print(car_1.wheels)
# print(car_2.wheels)



    # Inheritance (mostenirea) -- clasa copil va mosteni toate atributele si metodele clasei parinte


# class Animal:
#     alive = True
#
#     def eat(self):
#         print("This animal is eating")
#
#     def sleep(self):
#         print("This animal is sleeping")
#
# class Rabbit(Animal):
#
#     def run(self):
#         print("This rabbit is running")
#
# class Fish(Animal):
#
#     def swim(self):
#         print("This fish is swimming")
#
# class Hawk(Animal):
#
#     def fly(self):
#         print("This hawk is flying")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk =Hawk()
#
# # print(rabbit.alive)
# # fish.eat()
# # hawk.sleep()
#
# rabbit.run()
# fish.swim()
# hawk.fly()



    # Multi-level inheritance


# class Organism:
#     alive = True
#
# class Animal(Organism):
#
#     def eat(self):
#         print("This animal is eating")
#
# class Dog(Animal):
#
#     def bark(self):
#         print("This dog is barking")
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()



    # Multiple inheritance = when a child classs is derived from more than one parent class



# class Prey:
#
#     def flee(self):
#         print("This animal flees")
#
# class Predator:
#
#     def hunt(self):
#         print("This animal is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()



    # Method overriding


# class Animal:
#
#     def eat(self):  #method signature
#         print("This animal is eating")
#
#
# class Rabbit(Animal):
#
#     def eat(self):
#         print("This rabbit is eating a carrot")  #o sa o afiseze pe asta pentru ca e mai aproape
#
#
# rabbit = Rabbit()
# rabbit.eat()



    # Method chaining = calling multiple methods sequentially
                     #= each call performs an action on the same object and returns self


# class Car:
#
#     def turn_on(self):
#         print("You start the engine")
#         return self
#
#     def drive(self):
#         print("You drive the car")
#         return self
#
#     def brake(self):
#         print("You step on the brakes")
#         return self
#
#     def turn_off(self):
#         print("You turn off the engine")
#         return self
#
# car = Car()

# car.turn_on().drive()  #trebuie ca functia sa returneze self

# car.brake().turn_off()

# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()



        # Super function : super() Function used to give access to the methods of a parent class
        # returns a temporary object of a parent class when used


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
# class Square(Rectangle):
#
#     def __init__(self, length, width):
#         super().__init__(length, width)   #facem asta ca sa nu repetam codul
#     def area(self):
#         return self.length*self.width
#
# class Cube(Rectangle):
#
#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height
#     def volume(self):
#         return self.length*self.width*self.height
#
#
# square = Square(3,3)
# cube = Cube(3,3,3)
#
# print(square.area())
# print(cube.volume())



    # Abstract classes - prevents a user from creating an object of that class (ghost class)
    # + compels a user to override abstract methods in a child class
    # abstract class = a class which contains ore or more abstract methods
    # abstract method = a method that has a declaration but does not have an implementation

# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#
#     @abstractmethod
#     def go(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
#
# class Car(Vehicle):
#
#     def go(self):
#         print("You drive the car")
#
#     def stop(self):
#         print("This car is stopped")
#
#
# class Motorcycle(Vehicle):
#
#     def go(self):
#         print("You ride the motorcycle")  # concluzie : daca vrei sa mostenesti o metoda abstracta trebuie sa ii faci override
#
#     def stop(self):
#         print("This motorcycle is stopped")
#
# # vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# #vehicle.go()  #asta nu dorim, e ca si cum am crea masina invizibila in NFS
# car.go()
# motorcycle.go()
#
# car.stop()
# motorcycle.stop()



    # Objects as arguments


# class Car:
#     color = None
#
# def change_color(car,color):
#     car.color = color
#
#
# class Motorcycle:
#     color = "yellow"
#
#
# bike_1 = Motorcycle()
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
#
# change_color(car_1, "red")
# change_color(car_2, "white")
# change_color(car_3, "blue")
# change_color(bike_1, "black")
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)



    # Duck typing = concept where the class of an object is less important than the methods/attributes
    # class type is not checked if the minimum methods / attributes are present
    # "If it walks like a duck, and it quacks like a duck, then it must be a duck."


# class Duck:
#
#     def walk(self):
#         print("this duck is walking")
#
#     def talk(self):
#         print("this duck is qwacking")
#
# class Chicken:
#
#     def walk(self):
#         print("This chicken is walking")
#
#     def talk(self):
#         print("This chicken is clucking")
#
# class Person():
#
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter!")
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(chicken)


    # Walrus operator = assigns values to variables as a part of a larger expression


# happy = True
# print(happy)
#
# print(happy := True)

# foods = list()
# while True:
#     food = input("What food do u like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
# for x in foods:
#     print(x)


# foods = list()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)    #am observat ca daca incerc sa printez lista e lista de True



    # Function to variable


# def hello():
#     print("Hello")

# print(hello)
# hi = hello
# print(hi)

# hi = hello
# hi()
# hello()

# say = print
# say("Whoa!")



    # Higher Order Functions = a function that either:
    #                       1. accepts a function as an argument
    #                       or
    #                       2. returns a function
    #                       (in python functions are also treated as objects


# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
#
# hello(loud)
# hello(quiet)


# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend
#
#
# divide = divisor(2)
# print(divide(10))



    # Lambda function = function written in 1 line using lambda keyword
    #                   accepts any number of arguments, but only has one expression.
    #                 = shortcut
    #                 = (useful if needed fot a short period of time, throw-away
    # lambda parameters:expression

# def double(x):
#     return x * 2
#
# print(double(5))

# double = lambda x: x*2
# multiply = lambda x, y: x * y
# add = lambda x, y, z: x+y+z
# full_name = lambda first_name, last_name: first_name+" "+last_name
# age_check = lambda age: True if age >= 18 else False
#
#
# print(age_check(18))



    # Sort
    # sort() method = used with lists
    # sort() function = used with iterables

# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
#
# students.sort(reverse=True)
# for i in students:
#     print(i)


# students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")
# sorted_students = sorted(students, reverse=True)
# for i in sorted_students:
#     print(i)


# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr. Krabs", "C", 78)]
#
# grade = lambda grades: grades[1]   # asta ca sa le sortam alfabetic dupa a doua coloana
# students.sort(key=grade)           # aici pot pune ,reverse=True
# for i in students:
#     print(i)


# students = (("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr. Krabs", "C", 78))
#
# age = lambda ages: ages[2]
# sorted_students = sorted(students, key=age)
#
# for i in sorted_students:
#     print(i)



    # Map = applies a function to each item in an iterable (list, tuple, etc.)
    # mao(function, iterable)


# store = [("shirt", 20.00),
#          ("pants", 25.00),
#          ("jacket", 50.00),
#          ("socks", 10.00)]
#
# to_euros = lambda data: (data[0], data[1]*0.82)
# to_dollars = lambda data: (data[0], data[1]/0.82)
#
# store_euros = list(map(to_euros, store))
#
# for i in store_euros:
#     print(i)



    # Filter = creates a collection of elements from an iterable for which a function returns true
    # filter(function, iterable)


# friends = [("Rachel", 19),
#            ("Monica", 18),
#            ("Phoebe", 17),
#            ("Joey", 16),
#            ("Chandler", 21),
#            ("Ross", 20)]
#
# age = lambda data: data[1] >= 18
# drinking_buddies = list(filter(age, friends))
# for i in drinking_buddies:
#     print(i)

# def NumaraElemente(lista):
#     # Write your code here
#     s=0
#     for i in lista:
#         if isinstance(i, int):
#             s = s+1
#     if s==0:
#         print("-1")
#     else:
#         print(s)
#
# NumaraElemente(['one',2,3])

# def merge_sorted_arrays(arr1, arr2):
#     i = j = 0
#     merged_arr = []
#
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             merged_arr.append(arr1[i])
#             i += 1
#         else:
#             merged_arr.append(arr2[j])
#             j += 1
#     while i < len(arr1):
#         merged_arr.append(arr1[i])
#         i += 1
#
#     while j < len(arr2):
#         merged_arr.append(arr2[j])
#         j += 1
#
#     return merged_arr
#
# print(merge_sorted_arrays([1,2,3,5,8],[2,4,5,9]))

try:
    print("a")
except:
    print("b")
else:
    print("c")
finally:
    print("d")


















