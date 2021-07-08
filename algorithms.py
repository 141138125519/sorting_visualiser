import time
from colours import *


def bubble_sort(data, draw_data, time_tick):
    size = len(data)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, [yellow if x == j or x == j + 1 else blue for x in range(len(data))])
                time.sleep(time_tick)
    draw_data(data, [blue] * len(data))


# merge function for use in the following merge sort
def merge(data, start, mid, end):
    p = start
    q = mid + 1
    temp_array = []

    for i in range(start, end + 1):
        if p > mid:
            temp_array.append(data[q])
            q += 1
        elif q > end:
            temp_array.append(data[p])
            p += 1
        elif data[p] < data[q]:
            temp_array.append(data[p])
            p += 1
        else:
            temp_array.append(data[q])
            q += 1

    for p in range(len(temp_array)):
        data[start] = temp_array[p]
        start += 1


def merge_sort(data, start, end, draw_data, time_tick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, draw_data, time_tick)
        merge_sort(data, mid + 1, end, draw_data, time_tick)

        merge(data, start, mid, end)

        draw_data(data, [light_blue if start <= x < mid else yellow if x == mid
                         else dark_blue if mid < x <= end else blue for x in range(len(data))])
        time.sleep(time_tick)

    draw_data(data, [blue] * len(data))


# heapify function for the following heap sort
def heapify(data, n, i, draw_data):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[i] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        draw_data(data, [yellow if x == i or x == largest else blue for x in range(len(data))])

        heapify(data, n, largest, draw_data)


def heap_sort(data, draw_data, time_tick):
    length = len(data)

    for i in range(length//2, -1, -1):
        heapify(data, length, i, draw_data)
        draw_data(data, [yellow if x == i else blue for x in range(len(data))])
        time.sleep(time_tick)

    for i in range(length - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0, draw_data)
        draw_data(data, [yellow if x == i or x == 0 else blue for x in range(len(data))])
        time.sleep(time_tick)

    draw_data(data, [blue] * len(data))
