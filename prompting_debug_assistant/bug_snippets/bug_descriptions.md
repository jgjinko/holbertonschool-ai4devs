## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The function fails when n == len(items) because the starting index is calculated incorrectly.

## Bug 2 – bug2.js
**Intended Behavior**: Calculate the factorial of a number using recursion.  
**Issue Type**: Missing base case leading to infinite recursion.  
**Notes**: Input of 0 causes a stack overflow because it never reaches a termination condition.

## Bug 3 – bug3.cpp
**Intended Behavior**: Sort an array of integers using quicksort.  
**Issue Type**: Logic error (Poor pivot selection).  
**Notes**: Always selecting the first element as a pivot leads to O(n²) performance on already sorted arrays.

## Bug 4 – bug4.cs
**Intended Behavior**: Read lines from a file and count words.  
**Issue Type**: Logic error / Improper empty handling.  
**Notes**: Does not gracefully handle scenarios where the file might be empty, potentially leading to errors during string splitting.

## Bug 5 – bug5.java
**Intended Behavior**: Format a SQL query string using an array of parameters.  
**Issue Type**: Misuse of Data Types / Type Mismatch.  
**Notes**: Attempts to cast a primitive `int[]` array to `Object[]`, which causes a runtime ClassCastException in Java.

## Bug 6 – bug6.c
**Intended Behavior**: Find the maximum element in an integer array.  
**Issue Type**: Off-by-one error / Buffer overflow.  
**Notes**: The loop condition `i <= n` accesses memory outside the array bounds, leading to undefined behavior.