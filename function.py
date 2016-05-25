# -*- coding: utf-8 -*-
import random
import numpy
txt = 'random.txt'
# txt = 'in.txt'

'''
def sort1():
    in_txt = open(txt, 'r')
    output = open('out.txt', 'w')
    c = in_txt.read(1)
    my_list = []
    while len(c) > 0:
        if c != ' ' and c != '\n':
            my_list.append(c)
        c = in_txt.read(1)
    # print(my_list)
    my_list.sort(reverse=True)
    # print(my_list)
    i = 0
    for x in my_list:
        i += 1
        if i % 100 == 0:
            output.write('\n')
        output.write(x)
    in_txt.close()
    output.close()


def sort2():
    in_txt = open(txt, 'r')
    output = open('out.txt', 'w')
    my_list = in_txt.readlines()
    my_list.sort(reverse=True)
    # print(my_list)
    for x in my_list:
        output.write(x)
        output.write('\n')
    in_txt.close()
    output.close()
'''


def open_txt(file=txt):
    in_txt = open(file, 'r')
    # output = open('out.txt', 'w')
    my_list = in_txt.readlines()
    return my_list


def qsort(sort_list):
    less = []
    equal = []
    greater = []

    if len(sort_list) > 1:
        pivot = sort_list[0]
        for x in sort_list:
            if x > pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x < pivot:
                greater.append(x)
        # Don't forget to return something!
        return qsort(less) + equal + qsort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return sort_list


def create_sort_txt(sort_list):
    output = open('out.txt', 'w')
    for x in sort_list:
        output.write(x)
    output.close()


def create_txt():
    my_list = ['a', 'b', 'c', 'A', 'B', 'C', 'e', 'w', 'q', 'E', 'W', 'Q', 'v', 'x', 'z', 'V', 'X', 'Z']
    random_f = open('random.txt', 'w')
    for x in range(100000):
        for i in range(30):
            random_f.write(random.choice(my_list))
        random_f.write('\n')
    random_f.close()


def shell_sort(a):
    def new_increment(a):
        i = int(len(a) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(numpy.round(i/2.2))
            yield i
    for increment in new_increment(a):
          for i in range(increment, len(a)):
              for j in range(i, increment-1, -increment):
                  if a[j - increment] > a[j]:
                      break
                  a[j],a[j - increment] = a[j - increment],a[j]
    return a
