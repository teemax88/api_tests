# my_list = ['Peter', 'robot', 'Ivan', 'Sergey']
# my_list.sort(key=lambda x: x.lower())
# print(my_list)
# my_list.sort()
# print(my_list)

"""****************************//////////////////////////////************************"""

# class User():
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def greet(self):
#         print(f"Привет, {self.get_fullname()}!")
#
#     def get_fullname(self):
#         return f"{self.name} {self.surname}"
#
#     def __str__(self):
#         return self.get_fullname()
#
#
# user_1 = User('John', 'Perl')
# user_2 = User('Matt', 'Daymon')
#
# if __name__ == '__main__':
#     print(user_1.name)
#     print(user_2.name)
#     print(user_1)
# print(dir(__name__))


"""****************************//////////////////////////////************************"""

# def func(a, b, *args):
#     print(args)  # (1, 2, 3)
#     lst = list(args)
#     print(a, b, lst)  # 2 3 [1, 2, 3]
#
#
# func(2, 3, 1, 2, 3)

"""****************************//////////////////////////////************************"""

# n = 10
#
#
# def mother():
#     n = 20
#     a = 15
#
#     def son():
#         nonlocal a
#         a += 1  # 16
#         n = 30
#         print(n)    # будет выведено вторым: 30
#         print(locals())
#         print(a)
#
#     print(locals())  # будет выведено первым: {'n': 20, 'son': <function mother.<locals>.son at 0x0000023CAFF94900>, 'a': 15}
#     return son
#
#
# result = mother()
# result()

"""****************************//////////////////////////////************************"""


def sum_mul(n, m):
    s = 0
    if n <= 0 or m <= 0:
        return "INVALID"
    elif n <= 0 or m <= 0:
        return "INVALID"
    else:
        for i in range(n, m, n):
            s += i
    return s


print(sum_mul(2, 0))
