# -*- coding: utf-8 -*-
#Creating program for Bubble Sort 


def bubble_sort(arr):
    n = len(arr)
    
    for i in range(0,n):
        
        for j in range(0,n-i-1):
            
            if arr[j]>arr[j+1] :
                
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
arr = [1,5,3,8,6,9]

bubble_sort(arr)
for i in range(0,len(arr)):
    print(arr[i])