## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The function fails when n == len(items) due to an incorrect start_index calculation.

## Bug 2 – bug2.js
**Intended Behavior**: Calculate the factorial of a number using recursion.  
**Issue Type**: Logical error / Missing base case.  
**Notes**: The function lacks a base case for n == 0, causing infinite recursion and stack overflow.

## Bug 3 – bug3.cpp
**Intended Behavior**: Sort an array of integers using quicksort.  
**Issue Type**: Logical error.  
**Notes**: Always selecting the first element as the pivot results in O(n²) performance on sorted arrays.

## Bug 4 – bug4.cs
**Intended Behavior**: Read lines from a file and count words.  
**Issue Type**: Runtime exception / Null reference.  
**Notes**: The code does not handle empty files or null lines, leading to potential crashes during splitting.

## Bug 5 – bug5.java
**Intended Behavior**: Format a SQL query string using an array of parameters.  
**Issue Type**: Misuse of data types.  
**Notes**: Casting a primitive int[] to Object[] for String.format causes a runtime ClassCastException.

## Bug 6 – bug6.c
**Intended Behavior**: Find the maximum element in an integer array.  
**Issue Type**: Off-by-one error.  
**Notes**: The loop condition i <= n causes an out-of-bounds memory access at index n.