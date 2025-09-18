from abc import ABC, abstractmethod
# class Boss(ABC):
#     @abstractmethod
#     def task1(self):
#         pass
#     @abstractmethod
#     def task2(self):
#         pass
#     def sal(self):
#         print("Paid...50K")

# class Emp(Boss):
#     def task1(self):
#         print("Task1 Completed.")
#     def task2(self):
#         print("Task2 Completed.")

# emp1 = Emp()
# emp1.task1()
# emp1.task2()
# emp1.sal()

# Basic Level — Understanding Abstract Methods

# Task: Create an abstract class Animal with:

# sound() → abstract method

# Implement it in Dog and Cat classes
# Expected Output:
# Dog says Woof!
# Cat says Meow!

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow!")

dog = Dog()
cat = Cat()
dog.sound()
cat.sound()


# 2nd example 

# Task: Create an abstract class Appliance with:

# turn_on() → abstract

# brand() → normal method that prints brand name
# Create Fan and WashingMachine classes implementing turn_on().

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    def brand(self):
        print("Generic Appliance")

class Fan(Appliance):
    def turn_on(self):
        print("Fan is now ON")

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine is now ON")

fan = Fan()
washing_machine = WashingMachine()
fan.turn_on()
washing_machine.turn_on()
fan.brand()
washing_machine.brand()


# 3rd example 
# Polymorphism with Abstract Class

# Task: Create a payment system:

# Abstract class Payment with pay(amount)

# Classes: CreditCardPayment, UPIPayment, PayPalPayment
# Loop through a list of payment objects and process payments.

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment of {amount}")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of {amount}")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Processing PayPal payment of {amount}")

payments = [CreditCardPayment(), UPIPayment(), PayPalPayment()]
for payment in payments:
    payment.pay(100)
