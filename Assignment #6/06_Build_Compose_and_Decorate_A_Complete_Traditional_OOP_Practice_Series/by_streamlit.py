# 06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series
import streamlit as st
from abc import ABC, abstractmethod

# --- Classes ---

# 1. Student
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        return f"Student Name: {self.name}, Marks: {self.marks}"

# 2. Counter
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        return f"Objects Created: {cls.count}"

# 3. Car
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} car started."

# 4. Bank
class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# 5. MathUtils
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# 6. Logger
class Logger:
    def __init__(self):
        st.write("Logger Created.")

    def __del__(self):
        st.write("Logger Destroyed.")

# 7. Employee
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def display(self):
        return f"Name: {self.name}, Salary: {self._salary}"

# 8. Person/Teacher
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# 9. Shape/Rectangle
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

# 10. Dog
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

# 11. Book
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# 12. TemperatureConverter
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# 13. Engine/Vehicle
class Engine:
    def start(self):
        return "Engine started."

class Vehicle:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

# 14. Department/Staff
class Department:
    def __init__(self, employee):
        self.employee = employee

class Staff:
    def __init__(self, name):
        self.name = name

# 15. MRO
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):
    pass

# 16. Decorator function
def log_function_call(func):
    def wrapper():
        st.write("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    st.write("Hello!")

# 17. Class Decorator
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Individual:
    def __init__(self, name):
        self.name = name

# 18. Product
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

# 19. Multiplier
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

# 21. Countdown
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

# ------------------ Streamlit UI ------------------

st.title("06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series 🎯")

option = st.selectbox(
    "Choose Assignment to Test:",
    ("Student", "Counter", "Car", "Bank", "MathUtils", "Logger",
     "Employee", "Teacher", "Rectangle", "Dog", "Book",
     "TemperatureConverter", "Vehicle", "Department",
     "Diamond Inheritance (MRO)", "Function Decorator", "Class Decorator",
     "Product Property", "Multiplier", "Custom Exception", "Countdown")
)

if option == "Student":
    name = st.text_input("Enter Student Name:")
    marks = st.number_input("Enter Marks:", 0)
    if st.button("Show Student"):
        s = Student(name, marks)
        st.success(s.display())

elif option == "Counter":
    if st.button("Create Objects"):
        a = Counter()
        b = Counter()
        st.success(Counter.show_count())

elif option == "Car":
    brand = st.text_input("Enter Car Brand:")
    if st.button("Start Car"):
        car = Car(brand)
        st.success(car.start())

elif option == "Bank":
    if st.button("Change Bank Name"):
        Bank.change_bank_name("New Bank")
        st.success(f"Bank Name Changed: {Bank.bank_name}")

elif option == "MathUtils":
    a = st.number_input("Number A:", 0)
    b = st.number_input("Number B:", 0)
    if st.button("Add Numbers"):
        st.success(f"Sum: {MathUtils.add(a, b)}")

elif option == "Logger":
    if st.button("Create Logger"):
        log = Logger()

elif option == "Employee":
    name = st.text_input("Employee Name:")
    salary = st.number_input("Salary:", 0)
    ssn = st.text_input("SSN:")
    if st.button("Show Employee"):
        e = Employee(name, salary, ssn)
        st.success(e.display())

elif option == "Teacher":
    name = st.text_input("Teacher Name:")
    subject = st.text_input("Subject:")
    if st.button("Show Teacher"):
        t = Teacher(name, subject)
        st.success(f"{t.name} teaches {t.subject}")

elif option == "Rectangle":
    length = st.number_input("Length:", 0)
    width = st.number_input("Width:", 0)
    if st.button("Calculate Area"):
        r = Rectangle(length, width)
        st.success(f"Area: {r.area()}")

elif option == "Dog":
    name = st.text_input("Dog Name:")
    breed = st.text_input("Breed:")
    if st.button("Bark"):
        d = Dog(name, breed)
        st.success(d.bark())

elif option == "Book":
    if st.button("Add Book"):
        Book.increment_book_count()
        st.success(f"Total Books: {Book.total_books}")

elif option == "TemperatureConverter":
    celsius = st.number_input("Temperature in Celsius:", 0)
    if st.button("Convert"):
        st.success(f"Fahrenheit: {TemperatureConverter.celsius_to_fahrenheit(celsius)}")

elif option == "Vehicle":
    if st.button("Start Vehicle"):
        e = Engine()
        v = Vehicle(e)
        st.success(v.start())

elif option == "Department":
    emp_name = st.text_input("Employee Name:")
    if st.button("Show Department"):
        staff = Staff(emp_name)
        dept = Department(staff)
        st.success(f"Department Employee: {dept.employee.name}")

elif option == "Diamond Inheritance (MRO)":
    if st.button("Show MRO Result"):
        obj = D()
        st.success(obj.show())

elif option == "Function Decorator":
    if st.button("Say Hello"):
        say_hello()

elif option == "Class Decorator":
    if st.button("Greet from Decorator"):
        p = Individual("Tester")
        st.success(p.greet())

elif option == "Product Property":
    price = st.number_input("Enter Price:", 0)
    if st.button("Show Product Price"):
        p = Product(price)
        st.success(f"Price: {p.price}")

elif option == "Multiplier":
    factor = st.number_input("Factor:", 1)
    value = st.number_input("Value:", 1)
    if st.button("Multiply"):
        m = Multiplier(factor)
        st.success(f"Result: {m(value)}")

elif option == "Custom Exception":
    age = st.number_input("Enter Age:", 0)
    if st.button("Check Age"):
        try:
            check_age(age)
            st.success("Age is valid.")
        except InvalidAgeError as e:
            st.error(str(e))

elif option == "Countdown":
    start = st.number_input("Start Number:", 0)
    if st.button("Start Countdown"):
        output = [num for num in Countdown(start)]
        st.success(output)
