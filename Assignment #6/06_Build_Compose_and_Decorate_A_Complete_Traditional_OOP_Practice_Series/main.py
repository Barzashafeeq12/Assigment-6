# 06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

# 2. Using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Objects Created: {cls.count}")

# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started.")

# 4. Class Variables and Class Methods
class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger Created.")

    def __del__(self):
        print("Logger Destroyed.")

# 7. Access Modifiers
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn           # private

    def display(self):
        print(f"Name: {self.name}, Salary: {self._salary}")

# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# 9. Abstract Classes
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# 13. Composition
class Engine:
    def start(self):
        print("Engine started.")

class Vehicle:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

# 14. Aggregation
class Department:
    def __init__(self, employee):
        self.employee = employee

class Staff:
    def __init__(self, name):
        self.name = name

# 15. MRO and Diamond Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# 17. Class Decorators
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Individual:
    def __init__(self, name):
        self.name = name

# 18. Property Decorators
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return self.factor * x

# 20. Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")

# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

# ---------------------------------------------
# Test Section (You can comment/uncomment below)

if __name__ == "__main__":
    # 1
    s = Student("Alice", 90)
    s.display()

    # 2
    a = Counter()
    b = Counter()
    Counter.show_count()

    # 3
    car = Car("Toyota")
    print(car.brand)
    car.start()

    # 4
    b1 = Bank()
    b2 = Bank()
    print(b1.bank_name)
    Bank.change_bank_name("New Bank")
    print(b2.bank_name)

    # 5
    print(MathUtils.add(3, 5))

    # 6
    log = Logger()
    del log

    # 7
    emp = Employee("John", 50000, "123-45-6789")
    emp.display()
    print(emp.name)
    print(emp._salary)
    # print(emp.__ssn)  # Error

    # 8
    t = Teacher("Mr. Smith", "Math")
    print(t.name, t.subject)

    # 9
    r = Rectangle(5, 3)
    print(r.area())

    # 10
    d = Dog("Buddy", "Golden Retriever")
    d.bark()

    # 11
    Book.increment_book_count()
    print(Book.total_books)

    # 12
    print(TemperatureConverter.celsius_to_fahrenheit(0))

    # 13
    eng = Engine()
    v = Vehicle(eng)
    v.start()

    # 14
    staff = Staff("Emma")
    dept = Department(staff)
    print(dept.employee.name)

    # 15
    obj = D()
    obj.show()

    # 16
    say_hello()

    # 17
    p = Individual("Max")
    print(p.greet())

    # 18
    prod = Product(100)
    print(prod.price)
    prod.price = 150
    print(prod.price)
    del prod.price

    # 19
    m = Multiplier(3)
    print(m(5))
    print(callable(m))

    # 20
    try:
        check_age(17)
    except InvalidAgeError as e:
        print(e)

    # 21
    for num in Countdown(5):
        print(num, end=" ")
