# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:19:10 2020

@author: Nami_Kaneko
"""


def merge_arr(a, b):
    merged = []

    index_a = 0
    index_b = 0

    while index_a < len(a) and index_b < len(b):
        if a[index_a] > b[index_b]:
            merged.append(b[index_b])
            index_b += 1
        else:
            merged.append(a[index_a])
            index_a += 1
    if index_a == len(a):
        merged = merged + b[index_b: len(b)]
    else:
        merged = merged + a[index_a: len(a)]
    return merged


def merge_recursively(input_array):
    if len(input_array) == 1: return input_array[0]

    m = int((len(input_array)) / 2)
    print(m)
    a_half = input_array[0:m]
    b_half = input_array[m:len(input_array)]

    a_half = merge_recursively(a_half)
    b_half = merge_recursively(b_half)
    print(a_half)
    print(b_half)

    return merge_arr(a_half, b_half)


def merge_sort(input_array):
    sub_arrays = int((len(input_array) + 1) / 2)
    twod_arr = []
    index = 0
    if len(input_array) % 2 != 0:
        twod_arr.append([input_array[0]])
        index = 1
    for i in range(index, sub_arrays):
        twod_arr.append(input_array[index:index + 2])
        index += 2

    for i in range(len(twod_arr)):
        if len(twod_arr[i]) > 1 and (twod_arr[i][0] > twod_arr[i][1]):
            twod_arr[i][0], twod_arr[i][1] = twod_arr[i][1], twod_arr[i][0]

    return merge_recursively(twod_arr)


test_list = [1, 3, 2, 12, 4, 13, 12, 33, 2, 7, 6]

print(merge_sort(test_list))
