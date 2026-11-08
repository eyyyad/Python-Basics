
# =====================================
# Python Basics - My Learning Journey
# =====================================

# 1. Data Types

name = "Eyad"
number = 9

print(bool(name))
print(type([1, 1, 3, 4, 4, 4]))  # List
print(type({"one": 1, "two": 2}))  # Dictionary


# 2. Boolean

a = True
b = False

print(a or b)


# 3. Multiple Assignment

a, b, s = 1, 2, 3

print(a)
print(b)
print(s)


# 4. Escape Sequences

print("Hello love Python \"test\"")
print("Hello\nWorld")
print("Hello\tPython")
print("Hello Python")


# 5. String Concatenation

msg = "I love"
lang = " Python"

print(msg + lang)


# 6. Multiline Strings

text = """A
D "test"
F 'rm'
S"""

print(text)


# 7. String Slicing

name = "ilovepython"

print(name[::2])


# 8. Conditions

x = int(input("Please enter an integer: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")


# 9. Age Checker

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult")
else:
    print("You are under 18")


# 10. String Methods

text = "##eyad&&&&&&"

print(text.strip("&#"))

name = "eyad 6y u8 hosaam"
print(name.capitalize())


# 11. Zfill Method

c, a, v = "1", "10", "100"

print(c.zfill(3))
print(a.zfill(3))
print(v.zfill(3))
