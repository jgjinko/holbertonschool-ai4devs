## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The function calculates an incorrect starting index, causing it to skip the first element when the requested count equals the list length.

## Bug 2 – bug2.js
**Intended Behavior**: Calculate the factorial of a number using recursion.  
**Issue Type**: Runtime exception (Missing base case).  
**Notes**: The function lacks a base case for n equals 0, resulting in infinite recursion and a stack overflow.

## Bug 3 – bug3.cpp
**Intended Behavior**: Sort an array of integers using quicksort.  
**Issue Type**: Logical error (Poor pivot selection).  
**Notes**: Selecting the first element as the pivot consistently leads to O(n²) performance when the input array is already sorted.

## Bug 4 – bug4.cs
**Intended Behavior**: Read lines from a file and count words.  
**Issue Type**: Runtime exception (Null reference).  
**Notes**: The code fails to check if the file is empty or if lines are null before attempting to split the string, leading to a crash.

## Bug 5 – bug5.java
**Intended Behavior**: Format a SQL query string using an array of parameters.  
**Issue Type**: Misuse of data types.  
**Notes**: Attempting to cast a primitive `int[]` to `Object[]` for `String.format` causes a runtime ClassCastException in Java.

## Bug 6 – bug6.c
**Intended Behavior**: Find the maximum element in an integer array.  
**Issue Type**: Off-by-one error.  
**Notes**: The loop condition `i <= n` causes the program to access memory at index `n`, which is outside the array's bounds.