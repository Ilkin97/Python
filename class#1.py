# class Person
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def greeting(self):
        print(f"Hello my name is {self.name} and {self.age} years old.")

    def sleep(self):
        print(f"{self.name} go to the sleep.")


# class Animal
class Animal:
    def __init__(self, name, age, color) -> None:
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print(f"{self.name}, eating.")

    def run(self):
        print(f"{self.name} is run.")

# Person
if __name__ == "__main__":
    person1 = Person("Ilkin", 22)
    person1.greeting()
    person1.sleep()
#Animal
    animal1 = Animal("REX", 3, "black")
    animal1.eat()
    animal1.run()

# QUIZ
"""
1. What is a class in Python?
    a) A class is a built-in function.
    b) A class is an instance of an object.
    c) A class is a blueprint for creating objects.  +
    d) A class is a reserved keyword in Python.

2. In Python, which keyword is used to define a class?
    a) class +
    b) define
    c) struct
    d) object

3. How do you create an instance of a class in Python?
    a) By using the new keyword.
    b) By calling the class as a function. +
    c) By using the instance keyword.
    d) By using the class name followed by parentheses.
    
4. Which of the following statements is true regarding attributes in a class?
    a) Attributes are methods defined within a class.
    b) Attributes are used to create instances of a class.
    c) Attributes are variables that store data in a class. +
    d) Attributes are not allowed in Python classes.

5. Which keyword is used to access the attributes and methods of a class instance?
    a) access
    b) use
    c) this
    d) dot (.) +
    
6. How do you create an instance of a class in Python?
    a) By using the new keyword.
    b) By calling the class as a function. +
    
7. Which of the following statements is true regarding attributes in a class?
    a) Attributes are methods defined within a class.
    b) Attributes are variables that store data in a class. +
    
8. What is an "object" in the context of classes?
    a) An instance of a class. +
    b) A Python module.
    c) A function

9. What is the relationship between a class and an object in Python?
    a) A class is an instance of an object.
    b) An object is an instance of a class. +
    
10. What are "attributes" in a class?
    a) Functions defined within a class.
    b) Variables that store data within a class. +
    
11. In Python, how do you define a class?
    a) By using the class keyword followed by the class name and a colon.
    b) By using the def keyword followed by the class name and a colon. +
"""
