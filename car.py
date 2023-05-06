class Car:


    wheels = 4   #class variable  #declared within the class, but outside of the constructor


    def __init__(self, make, model, year, color):  #constructor
        self.make = make     #instance variables  #declared inside of the constructor ; they can be given unique values
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")