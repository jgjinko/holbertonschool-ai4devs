## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one or loop logic issues.  
**Notes**: Incorrect start_index calculation causes the function to skip the first item when n equals the list length.

## Bug 2 – bug2.js
**Intended Behavior**: Calculate the factorial of a number using recursion.  
**Issue Type**: Runtime exceptions.  
**Notes**: Missing base case for n equals 0 results in infinite recursion and a stack overflow.

## Bug 3 – bug3.cpp
**Intended Behavior**: Sort an array of integers using quicksort.  
**Issue Type**: Logical errors.  
**Notes**: Selecting the first element as the pivot leads to O(n²) performance on already sorted arrays.

## Bug 4 – bug4.cs
**Intended Behavior**: Read lines from a file and count words.  
**Issue Type**: Runtime exceptions.  
**Notes**: Lack of validation for empty files or null lines leads to potential NullReferenceExceptions during string splitting.

## Bug 5 – bug5.java
**Intended Behavior**: Format a SQL query string using an array of parameters.  
**Issue Type**: Misuse of data types or libraries.  
**Notes**: Casting a primitive int[] array to Object[] for String.format causes a runtime ClassCastException.

## Bug 6 – bug6.c
**Intended Behavior**: Find the maximum element in an integer array.  
**Issue Type**: Off-by-one or loop logic issues.  
**Notes**: The loop condition i <= n causes an out-of-bounds access at index n.