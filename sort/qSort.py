import random
import time
import sys


def swap(a, b):
    a, b = b, a

def partition_arr(arr, start, end, win, fun):

    fun(win, arr)

    # time.sleep(20)
    pivot = arr[end].height
    p_index = start

    for i in range(start, end):
        if arr[i].height <= pivot:
            arr[i].height, arr[p_index].height = arr[p_index].height, arr[i].height
            p_index += 1

    arr[p_index].height, arr[end].height = arr[end].height, arr[p_index].height

    return p_index



def q_sort(arr, start, end, win, fun):
    # fun(win, arr)

    if(start < end):
        p_index = partition_arr(arr, start, end, win, fun)
        q_sort(arr, start, p_index-1, win, fun)
        q_sort(arr, p_index+1, end, win, fun)
    
