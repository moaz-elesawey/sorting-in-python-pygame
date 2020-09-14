def swap(a, b):
    a, b = b, a

def bubble_sort(arr, n, win, fun):

    while True:
        
        fun(win, arr)

        done = False

        for i in range(0, n):
            if arr[i].height > arr[i+1].height:

                arr[i].height, arr[i+1].height = arr[i+1].height, arr[i].height

                done = True

        if not done:
            break
