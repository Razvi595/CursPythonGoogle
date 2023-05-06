class Animal(object):


    def __init__(self, age):

        self.years = age
        self.name = None

    def get_age(self):
        return self.years

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.years = new_age

    def __str__(self):
        return f"animal: {self.name}, {self.years}"


class Cat(Animal):
    def speak(self):
        print("Miau")

    def __str__(self):
        return f"cat : {self.name}, {self.years}"


a = Animal(7)
a.set_name("Jerry")
a.set_age(9)
print(a)


cat = Cat(5)
cat.set_name("Tom")
print(cat)
cat.speak()




