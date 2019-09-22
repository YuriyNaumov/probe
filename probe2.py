# print('дратути')
# my_famaly_height = [
#     ['мама', 186],
#     ['папа', 198],
#     ['я', 200]
# ]

# print(type(my_famaly_height))

# print(type(my_famaly_height[0]))


import simple_draw


# b = -5


#
# if 0 < b < 10:
#     print(b)
# else:
#     print('нет данных')
#
# myzoo = ['cat', 'lion', 'tiger']
#
# for i in myzoo:
#     if i == 'cat':
#         myzoo.append('dog')
#
# print(myzoo)


# i = 10
# while i < 15:
#     print('i=', i)
#     i += 1

# f1, f2 = 1, 1
# print(f1)
#
# while f2 < 1000:
#     print(f2)
#     f1, f2 = f2, f1 + f2


# i = 1
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#
#     print(i)
# else:
#     print('i=',i)


# for a, b in [(1, 3), (2, 4), (4, 5)]:
#     print(a+b)

# animals = ['tiger','lion', 'cat', 'dog', 'skunk']
#
# for i, animal in enumerate(animals):
#     print(i)
#     print(animal)

def create_users():
    """this function returns age and name"""
    name = 'иван'
    age = 27
    return name, age


# name, age = create_users()
# print(name, age)
create_users()
import random
import simple_draw as sd

sd.resolution = (1200, 600)


def bubble(point, step):
    radius = 50
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, width=2)
        radius += step


for y in range(100, 500, 100):
    for x in range(100, 1000, 100):
        point = sd.random_point()
        step = random.randint(2, 50)
        bubble(point, step)

sd.pause()


