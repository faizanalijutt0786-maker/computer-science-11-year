---
id: chapter-2
title: "Chapter 2: Python Programming"
sidebar_label: "Chapter 2: Python Programming"
sidebar_position: 2
---

# Unit 2: Python Programming

## Student Learning Outcomes

By the end of this chapter, students will be able to:

- Understand basic programming concepts and set up a Python development environment.
- Write and interpret basic Python syntax and structure, including variables, data types, and input/output operations.
- Use various operators and expressions in Python, including arithmetic, comparison, and logical operators.
- Implement control structures such as decision-making statements and loops in Python.
- Work with Python modules, functions, and built-in data structures like lists.
- Apply modular programming techniques and object-oriented programming concepts in Python.
- Handle exceptions, perform file operations, and apply testing and debugging techniques in Python.

## Introduction

Python is a popular and easy-to-learn programming language. In this unit, you will learn the basics, setup tools and explore key components. Later, we will learn advanced topics like file handling, debugging and data structures.

---

## 2.1 Introduction to Python Programming

Python is versatile and applicable to various fields, including web development, data analysis, artificial intelligence, and more. Python's straightforward syntax and clear structure make it an excellent choice for beginners, allowing them to focus on learning programming concepts rather than dealing with complex syntax rules.

### 2.1.1 Understanding Basic Programming Concepts

Computer programming is the process of creating a set of instructions that tell a computer how to perform a task. These instructions are written in a programming language that the computer can understand and execute.

#### 2.1.1.1 Programming Basics

Computer programming involves the following basic steps to write a program:

1. **Write Code:** Create a set of instructions in a programming language.
2. **Compile/Interpret:** Translate the code into a form that the computer can understand.
3. **Execute:** Run the code to perform the task.
4. **Output:** Display the results or perform actions based on the code.

#### 2.1.1.2 Setting Up Python Development Environment

The development environment refers to the process of preparing a computer to write, run, and debug Python code effectively. This involves installing and configuring the necessary software, tools, and libraries. We can download and install Python from https://www.python.org/.

When starting with Python programming, choosing an Integrated Development Environment (IDE) can help make coding easier.

> **Tidbits:** When installing Python, make sure to check the box that says "Add Python to PATH." This makes it easier to run Python from the command line. We can also use online services to write and run Python programs.

---

## 2.2 Basic Python Syntax and Structure

The following Python program demonstrates the simplicity and readability of the language:

```python
print("This is my first program")
```

In this example, the `print` function is utilized to output the message enclosed in double quotation marks. This illustrates Python's straightforward syntax, where a function like `print` is used to perform actions such as displaying text.

### Python Comments

Lines that are not executed by the Python interpreter. They are used to provide explanations or notes for the code. Single-line comments start with the `#` symbol, while multi-line comments can be created using triple quotes at the beginning and the end:

```python
# This is a single-line comment
print("K2 is the second-highest mountain in the world")

"""
This is a multi-line comment
It can span multiple lines
"""
"Edhi Foundation is the largest volunteer ambulance network"
```

### 2.2.1 Variables, Data Types and Input/Output

#### 2.2.1.1 Variable

A variable is a storage container in a computer's memory that allows storage, retrieval and manipulation of data. The value of a variable can change throughout the execution of a program:

```python
age = 71
print("Ahmad lived for", age, "years")
age = 60
print("Iqbal lived for", age, "years")
```

#### 2.2.1.2 Variable Naming Rules in Python

Variable names in Python must adhere to the following rules:

- The name must begin with a letter (a-z, A-Z) or an underscore (`_`).
- Subsequent characters can include letters, digits (0-9), or underscores (`_`).
- Variable names are case-sensitive; meaning `age` and `Age` are considered two different variables.
- Python's reserved keywords, such as `for`, `while`, `if`, etc., cannot be used as variable names.

> **Tidbits:** Always use meaningful names for variables to make your code easier to understand. For example, use `age` instead of `a`.

#### 2.2.1.3 Creating Different Types of Variables

In Python, you can create variables of different types to store various kinds of data. Here are some common types:

- **Integer (int):** Stores whole numbers. Example: `age = 17`
- **Floating-point (float):** Stores decimal numbers. Example: `price = 19.99`
- **String (str):** Stores text. Example: `name = "Ali"`
- **Boolean (bool):** Stores True or False. Example: `is_student = True`

> **Tidbits:** It's a good practice to use lowercase letters for variable names and underscores to separate words (e.g., `student_name`).

#### 2.2.1.4 Input and Output Operations

Input and output operations allow you to interact with the user.

- **Input:** Use the `input()` function to get user input. It displays a message on the screen and waits for the user to type something and press Enter:

```python
name = input("Enter your name: ")
```

- **Output:** Use the `print()` function to display information on the screen:

```python
print("Hello", name)
```

#### 2.2.1.5 Handling Integer and Float Inputs

To handle numeric inputs, use `int()` or `float()` functions to convert input strings:

```python
# Integer input
user_age = int(input("Enter your age: "))
print("Your age is:", user_age)

# Float input
user_height = float(input("Enter your height in meters: "))
print("Your height is", user_height, "meter")
```

---

## 2.3 Operators and Expressions

Operators are symbols that perform operations on variables and values. An expression is a combination of variables, operators, and values that produces a result.

### 2.3.1 Arithmetic Operators

Arithmetic operators are used to perform basic mathematical operations:

```python
a = 10
b = 3

print(a, "+", b, "=", a + b)   # Output: 10 + 3 = 13
print(a, "*", b, "=", a * b)   # Output: 10 * 3 = 30
print(a, "/", b, "=", a / b)   # Output: 10 / 3 = 3.3333...
print(a, "//", b, "=", a // b) # Output: 10 // 3 = 3
print(a, "%", b, "=", a % b)   # Output: 10 % 3 = 1
print(a, "**", b, "=", a ** b) # Output: 10 ** 3 = 1000
```

### 2.3.2 Comparison Operators

Comparison operators are used to compare two values or expressions. They return a boolean value (True or False):

```python
x = 10
y = 7

print(x, ">", y, "=", x > y)   # Output: 10 > 7 = True
print(x, "<", y, "=", x < y)   # Output: 10 < 7 = False
print(x, "==", y, "=", x == y) # Output: 10 == 7 = False
print(x, "!=", y, "=", x != y) # Output: 10 != 7 = True
print(x, ">=", y, "=", x >= y) # Output: 10 >= 7 = True
print(x, "<=", y, "=", x <= y) # Output: 10 <= 7 = False
```

### 2.3.3 Assignment Operators

Assignment operators are used to assign values to variables. The most common is `=`. There are also compound assignment operators:

```python
a = 10
b = 5

a += b  # a = 15
a -= b  # a = 10
a *= b  # a = 50
a /= b  # a = 2.0
a %= b  # a = 0
a **= b # a = 100000
```

### 2.3.4 Logical Operators

Logical operators are used to combine multiple conditions. The most common are `and`, `or`, and `not`:

```python
x = True
y = False

logical_and = x and y
print(x, "and", y, "=", logical_and)  # Output: True and False = False

logical_or = x or y
print(x, "or", y, "=", logical_or)    # Output: True or False = True

logical_not = not x
print("not", x, "=", logical_not)     # Output: not True = False
```

### 2.3.5 Expressions

An expression is a combination of variables, operators, and values that produces a result. For example, `3 + 4` is an expression that results in `7`. More complex expressions can use parentheses to control the order of operations:

```python
result = (3 + 4) * 2  # result is 14
```

> **Class Activity:** Write a program to calculate Body Mass Index (BMI). Ask the user for their weight and height, then compute and display their BMI using: BMI = weight / height²

### 2.3.6 Operator Precedence in Python

Operator precedence determines the order in which operations are performed:

1. **Parentheses `()`** — Highest precedence. `(1 + 2) * 4` evaluates to 12.
2. **Exponentiation `**`** — `2 ** 3` evaluates to 8.
3. **Multiplication `*`, Division `/`, Modulus `%`** — `4 * 3` = 12, `10 / 2` = 5.0.
4. **Addition `+` and Subtraction `-`** — Lowest precedence. `5 + 2` = 7.

> **Class Activity:** Compute the following expressions:
> 1. `10 + 3 * 2 ** 2 - 5 / 5`
> 2. `(10 + 3) * (2 * (2 - 1) / 5)`

---

## 2.4 Control Structures

In programming, we often need to control the flow of our program based on different conditions or repeat certain actions multiple times. There are two main types: **Decision Making** and **Looping**.

### 2.4.1 Decision Making

#### 2.4.1.1 If Statement

The `if` statement allows us to make decisions based on conditions:

```python
temperature = 35
if temperature > 30:
    print("It is a hot day")
```

#### 2.4.1.2 If-else Statement

The `if-else` statement executes one block if a condition is true and another if false:

```python
temperature = 15
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
```

#### 2.4.1.3 Short-hand If-else Statement

Python also allows a short-hand if-else statement in a single line:

```python
temperature = 15
m = "It's a hot day" if temperature > 30 else "It's not a hot day"
print(m)
```

> **Class Activity:** Write an if-else statement and a short-hand if-else statement to check if a number is even or odd.

#### 2.4.1.4 if-elif-else Statement

The `if-elif-else` statement allows checking multiple conditions:

```python
weather = "cloudy"
if weather == "sunny":
    print("Wear sunglasses")
elif weather == "rainy":
    print("Take an umbrella")
else:
    print("Enjoy your day!")
```

> **Class Activity:** Write an if-elif-else statement to check if a number is positive, negative, or zero.

---

### 2.4.2 Looping Constructs

Loops help us repeat actions, making code more efficient and easier to read.

#### 2.4.2.1 while Loop

A `while` loop runs as long as a condition is true:

```python
number = 1
while number <= 10:
    print(number)
    number += 1
```

> **Class Activity:** Write a Python program that prints even numbers and counts the odd numbers from 1 to 20 using a while loop.

#### 2.4.2.2 for Loop

A `for` loop repeats a block of code over a sequence:

```python
friends = ["Ahmad", "Ali", "Hassan"]
for friend in friends:
    print("Hello", friend)
```

> **Class Activity:**
> 1. Write a for loop using `range()` to print even numbers from 2 to 10.
> 2. Write a Python program that prints the first 10 multiples of 3 using a for loop and the `range()` function.

---

## 2.5 Python Modules and Built-in Data Structures

Python offers an extensive standard library that includes numerous built-in modules and data structures.

### 2.5.1 Functions and Modules

#### 2.5.1.1 Defining and Invoking Functions

Functions are defined using the `def` keyword:

```python
def greet(name):
    print("Hello", name)

greet('Ali')
```

#### 2.5.1.2 Function Parameters and Return Values

Functions can take multiple parameters and return values:

```python
def add(a, b):
    return a + b
```

> **Do You Know?** You can call a function multiple times with different arguments to reuse the same code for different inputs.

#### 2.5.1.3 Default Parameters

Functions can have default parameter values:

```python
def greet(name="Student"):
    return "Hello, " + name + "!"

print(greet())        # Output: Hello, Student!
print(greet("Umed"))  # Output: Hello, Umed!
```

> **Class Activity:** Define a function that takes a list of numbers and returns the maximum value.

### 2.5.2 Using Libraries and Modules

In Python, libraries and modules are like toolboxes full of useful tools.

### 2.5.3 Importing and Using Libraries

```python
import random
number = random.randint(1, 10)
print("The random number is:", number)

import datetime
current_time = datetime.datetime.now()
print("Current date and time:", current_time)

import statistics
data = [23, 45, 67, 89, 12, 44, 56]
mean_value = statistics.mean(data)
print("The mean value is:", mean_value)
```

#### 2.5.3.1 Package Structure

To manage large projects, you can organize modules into packages:

```python
# In ecommerce/products.py:
def list_products():
    return ["Laptop", "Mobile", "Tablet"]

# In your main script:
from ecommerce import products
available_products = products.list_products()
print(available_products)
# Output: ['Laptop', 'Mobile', 'Tablet']
```

> **Tidbits:** Organizing your modules into packages is like organizing books into sections of a library — it makes finding and maintaining your code much easier.

---

## 2.6 Built-in Data Structures

### 2.6.1 Lists

A list is a versatile data structure that can hold a collection of items.

#### 2.6.1.1 Creating, Accessing, and Modifying Lists

```python
fruits = ["Mango", "Apple", "Banana"]
print(fruits)  # Output: ['Mango', 'Apple', 'Banana']
```

#### 2.6.1.2 Accessing List Items

```python
fruits = ["Mango", "Apple", "Banana"]
print(fruits[1])  # Output: Apple
```

#### 2.6.1.3 Modifying a List

```python
fruits = ["Mango", "Apple", "Banana"]
fruits[0] = "Orange"
fruits.append("Pineapple")
print(fruits)  # Output: ['Orange', 'Apple', 'Banana', 'Pineapple']
```

#### 2.6.1.4 Methods and Operations on Lists

- `append(item)` — Adds an item to the end of the list.
- `remove(item)` — Removes the first occurrence of an item.
- `sort()` — Sorts the list in ascending order.
- `reverse()` — Reverses the order of the list.

```python
students = ["Ahmed", "Sara", "Ali"]
students.append("Hina")
students.sort()
print(students)  # Output: ['Ahmed', 'Ali', 'Hina', 'Sara']
```

#### 2.6.1.5 List Operations

```python
numbers = [1, 2, 3, 4, 5]
sliced = numbers[1:4]       # Gets items from index 1 to 3
extra_numbers = [6, 7]
combined = sliced + extra_numbers
print(combined)             # Output: [2, 3, 4, 6, 7]
```

> **Class Activity:** Maintain a list of your favorite books: `["To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice"]`. Perform:
> 1. Add "Moby Dick" to the list.
> 2. Replace "1984" with "Brave New World".
> 3. Remove "The Great Gatsby".
> 4. Merge with `["War and Peace", "Hamlet"]`.
> 5. Print the final list.

### 2.6.2 Tuples

Tuples are like lists but **immutable** — their values cannot be changed after creation:

```python
my_tuple = (1, 2, 3, "Hello", 4.5)
print(my_tuple[0])    # Output: 1
print(my_tuple[3])    # Output: Hello
print(len(my_tuple))  # Output: 5
```

### 2.6.3 Indexing and Slicing

#### 2.6.3.1 Indexing

Python uses zero-based indexing — the first element has index `0`.

#### 2.6.3.2 Slicing

```python
sequence[start:stop:step]
```

#### 2.6.3.3 Indexing and Slicing with Negative Indices

Negative indices count from the end. `-1` refers to the last element.

```python
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

print("First fruit:", fruits[0])       # Positive index
print("Last fruit:", fruits[-1])       # Negative index
print("Fruits from index 1 to 3:", fruits[1:4])
print("Fruits from index -4 to -1:", fruits[-4:-1])
```

---

## 2.7 Modular Programming in Python

Modular programming is a technique used to divide a program into smaller, manageable, and reusable pieces called modules.

### The main Function

```python
# main.py
def main():
    print("This is the main function")

if __name__ == "__main__":
    main()
```

> **Do You Know?** Python's standard library is made up of hundreds of modules that you can use to perform common tasks, like working with dates, generating random numbers, or reading files.

> **Activity:** Create a Python module named `calculator.py` that includes:
> 1. `add(a, b)` — returns the sum of two numbers.
> 2. `subtract(a, b)` — returns the difference between two numbers.
> Then write a `main.py` that imports and uses these functions.

---

## 2.8 Object-Oriented Programming in Python

Object-Oriented Programming (OOP) is a way of designing and organizing code to make it easier to manage and understand.

### 2.8.1 Class and Objects

A **class** is like a template for creating things, and an **object** is an actual thing created from that template.

#### 2.8.1.1 Defining Classes and Creating Objects

```python
class ToyCar:
    def __init__(self, color, size, wheels):
        self.color = color
        self.size = size
        self.wheels = wheels

    def describe(self):
        return f"This toy car is {self.color}, size {self.size}, and has {self.wheels} wheels"

car1 = ToyCar("red", "small", 4)
car2 = ToyCar("blue", "large", 4)

print(car1.describe())
print(car2.describe())
```

**Key concepts:**
- **Class Definition:** `ToyCar` is the template describing what attributes a toy car should have.
- **Creating Objects:** `car1` and `car2` are specific toy car objects created using the `ToyCar` template.
- **Using Methods:** The `describe()` method gives a description of the toy car.
- **Self:** `self` is a convention used in OOP to represent the instance of a class within its methods.

---

## 2.9 Advanced Python Concepts

### 2.9.1 Exception Handling

Exception handling is a mechanism to manage errors that occur during program execution.

#### 2.9.1.1 Try-Except Blocks

```python
a = int(input("Enter a number: "))
try:
    result = 10 / a
except ZeroDivisionError:
    print("You can't divide by zero!")
```

The `try` block contains code that might cause an error. The `except` block catches the error and handles it gracefully.

#### 2.9.1.4 File Handling

File handling involves reading from and writing to files.

#### 2.9.1.5 Opening, Reading, and Closing Files

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

The `with` statement ensures the file is properly closed after use, even if an error occurs.

#### 2.9.1.6 Writing to Files

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("As-Salaam-Alaikum, World!\n")

# Appending to a file
with open("example.txt", "a") as file:
    file.write("Appending new line.\n")
```

---

## 2.10 Testing and Debugging in Python

### 2.10.1 Testing

Testing is the process of running your code with various inputs to check if it behaves as expected.

#### 2.10.1.1 Types of Testing

- **Unit Testing:** Tests individual parts of the code (like functions or classes) in isolation. Python's `unittest` module is commonly used.
- **Integration Testing:** Checks how different parts of the code work together.
- **Functional Testing:** Validates that the software behaves as expected from the user's perspective.
- **Regression Testing:** Ensures that new changes don't break existing functionality.

#### 2.10.1.2 Debugging

Debugging is the process of finding and fixing errors (bugs) in your code.

#### 2.10.1.3 Common Debugging Techniques

- **Print Statements:** Adding `print()` statements to check the values of variables at different stages.
- **Debugging Tools:** Using tools like `pdb` (Python Debugger) to step through the code.
- **Error Messages:** Reading and understanding error messages to locate the source of the problem.

---

## Exercise

### Multiple Choice Questions

1. An action needed during Python installation to run from the command line easily:
   - a) Uncheck "Add Python to PATH"
   - b) Choose a different IDE
   - **c) Check "Add Python to PATH"**
   - d) Install only the IDE

2. A valid variable name in Python is:
   - **a) variable1**
   - b) 1variable
   - c) variable-name
   - d) variable name

3. Output of: `age = 25; print("Age:", age)`:
   - **a) Age: 25**
   - b) 25
   - c) Age

4. The operator used for exponentiation in Python:
   - a) ^
   - **b) \*\***
   - c) //

5. A loop used to iterate over a collection such as lists:
   - a) while
   - **b) for**
   - c) do-while
   - d) repeat

6. The `range()` function:
   - a) Generates a list of numbers
   - **b) Creates a sequence of numbers**
   - c) Calculates the sum of numbers

7. A keyword used to define a function in Python:
   - a) define
   - b) function
   - **c) def**
   - d) func

8. Output of:
```python
temperature, humidity, wind_speed = 25, 60, 15
print("Hot and humid" if temperature > 30 and humidity > 50 else
      "Warm and breezy" if temperature == 25 and wind_speed > 10 else
      "Cool and dry" if temperature < 20 and humidity < 30 else
      "Moderate")
```
   - a) Hot
   - **b) Warm and breezy**
   - c) Cool
   - d) Moderate

9. The operation used to combine two lists in Python:
   - a) combine()
   - b) concat()
   - **c) +**
   - d) merge()

### Short Questions

1. Explain the purpose of using comments in Python code.
2. Describe the difference between integer and float data types in Python. Provide an example of each.
3. Define operator precedence and give an example of an expression where operator precedence affects the result.
4. How does the short-hand if-else statement differ from the regular if-else statement?
5. Explain the use of the `range()` function in a `for` loop.
6. Explain how default parameters work in Python functions.
7. Explain why modular programming is useful in Python.
8. Explain the difference between a class and an object in Python.

### Long Questions

1. Evaluate the following Python expressions:
   - (a) `(18 / 3 + 4 * 2) - (2 * (7 - 3)) / (9 - 4)`
   - (b) `(25 + 3 * 4 ** 2 - 6) / (2 ** 3 + 1) - 7`
   - (c) `(12 + 6 * (5 - 2)) ** 2 / ((4 ** 2 - 7) + 10)`
   - (d) `45 / (2 ** 2 + 3 * 4) + 8 * (7 - 3)`

2. Translate the following mathematical expressions to Python syntax:
   - (a) `5 × (x + 2)`
   - (b) `7 + 2²`

3. Explain the concept of variables in Python.

4. Write a Python program that takes a number as input and checks whether it is positive, negative, or zero using an if-elif-else statement.

5. Write a Python program using a while loop that prints all the odd numbers between 1 and 100. Also, count and print the total number of odd numbers.
