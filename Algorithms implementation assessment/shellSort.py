# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:33:47 2022

@author: ikhwan
"""

# Shell sort
# argument arr = array
def shellSort(arr):
    
    # initialize gap
    gap = len(arr) // 2
    
    # rearrange elements at each n/2, n/4, n/8, ... gap
    # swap values if not in the right order
    while gap > 0:
        for i in range(gap, len(arr)):
            j = i
            temp = arr[i]
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
        
# testing
data = [9, 8, 3, 7, 5, 6, 4, 1]
shellSort(data)
print('Sorted Array in Ascending Order:')
print(data)