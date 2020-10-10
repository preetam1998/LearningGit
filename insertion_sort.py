# -*- coding: utf-8 -*-
"""
Writing program for the insertion Sort ....
In Python
"""
def insertion_sort(arr):
  
    for i in range(1,len(arr)):
        
         j = i-1
         x = arr[i]
         while j>-1  and arr[j] > x :
             arr[j+1] = arr[j]
             j = j - 1
         arr[j+1] = x
            
arr = [1,5,3,8,6,9]
insertion_sort(arr)
for i in range(0,len(arr)):
    print(arr[i])