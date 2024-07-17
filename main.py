"""
Lesson 3 Closures Git and Github
"""
# a = 25
# z = 15
#
#
# def outer(x):
#     def inner():
#         nonlocal a
#         global z
#         a += 1
#         print("Inner func x = ", x)
#         print("a = ", a)
#     return inner
#


def calculator(a: int, b: int):

    def main():
        print("Setting")

    def plus():
        return a + b

    main.plus = plus
    return main


calc = calculator(15, 20)
print(calc.plus())
