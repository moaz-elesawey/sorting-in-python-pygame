def merge_sort(arr, win, fun):
    
    if len(arr) >1:
        
        m = len(arr) // 2

        L = arr[:m]
        R = arr[m:]

        merge_sort(L, win, fun)
        merge_sort(R, win, fun)

        i = j = k = 0

        while i < len(L) and j < len(R):
            fun(win, arr)
            if L[i] < R[j]:
                temp = arr[k]
                temp.height = L[i].height
                i += 1
            else:
                temp = arr[k]
                temp.height = R[j].height
                j += 1
            k += 1
            
        while i < len(L): 
            arr[k] = L[i]
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j]
            j+= 1
            k+= 1
