# what is classes? - In programming, a class is a blueprint or template for creating objects (instances). It defines a set of attributes (data) and methods (functions) that the objects created from the class will have. Classes are a fundamental concept in object-oriented programming (OOP) and are used to model real-world entities or concepts in code.
# what is objects? - In programming, an object is an instance of a class. It is a concrete entity created from a class blueprint, and it contains both data (attributes) and behavior (methods) defined by the class. Objects are fundamental to object-oriented programming (OOP) and allow developers to model real-world entities or concepts in code.

class car:
    model = "thar"
    price = "20lac"

    def carinfo(self):
        print(f"{self.model} is the model of car and the price of this is {self.price}")


car1 = car()
car1.model = "maruti"
car1.price = "10 lac"

car2 = car()
car2.model = "BMW"
car2.price = "2 cr"

car1.carinfo()
car2.carinfo()

# what is self? - self allows you to access and modify the instance's attributes and call its methods.
#It ensures that the correct instance's data is being used when multiple objects of the same class exist


#What is constructor?- A constructor is a special method in a class that is automatically called when an object (instance) of the class is created.
#In Python, class has __init__() function. It automatically initializes object attributes when an object is created.
class new_car:

    def __init__(self, m, p):
        self.car_model = m 
        self.car_price = p

        print(f"model of my car is {self.car_model} and price of this is {self.car_price}")
        

    def info(self):
        self.car_name = "indigo"
        print(f"my car is {self.car_name}")

new_car1 = new_car("swift", "15lac")
new_car1.info()


#what is decorators? - Decorators in Python are a powerful and flexible way to modify or extend the behavior of functions



  
