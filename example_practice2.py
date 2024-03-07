lst = [1, -2, -5, 3, 4, 5, 6, 8, 9, 11]

lst.sort(reverse=True)  # сортировка в убывающем порядке
print(lst)  # Вывод: [11, 9, 8, 6, 5, 4, 3, 1, -2, -5]
n = 4
for k, v in enumerate(lst):
    print(f"Индекс {k} == {v}")

"""
Индекс 0 == 11
Индекс 1 == 9
Индекс 2 == 8
Индекс 3 == 6
Индекс 4 == 5
Индекс 5 == 4
Индекс 6 == 3
Индекс 7 == 1
Индекс 8 == -2
Индекс 9 == -5
"""



# for i in range(10):
    # lst.append(int(input()))


# print(lst)
# print(lst.index(5))
#
#
# # for j in lst:
# #     print(j)