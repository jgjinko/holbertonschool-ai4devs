## Bug 1 – bug1.py

**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The function fails when n == len(items).

## Bug 2 – bug2.js

**Intended Behavior**: Calculate the factorial of a number using recursion.  
**Issue Type**: Missing base case leading to infinite recursion.  
**Notes**: Input of 0 causes a stack overflow.

## Bug 3 – bug3.cpp

**Intended Behavior**: Sort an array of integers using quicksort.  
**Issue Type**: Incorrect pivot selection causing poor performance.  
**Notes**: Worst-case O(n²) behavior on already sorted arrays.

## Bug 4 – bug4.cs

**Intended Behavior**: Read lines from a file and count words.  
**Issue Type**: Null reference when file is empty.  
**Notes**: Does not handle empty or missing files gracefully.

## Bug 5 – bug5.java

**Intended Behavior**: Connect to a database and execute a query.  
**Issue Type**: Resource leak due to not closing connection.  
**Notes**: May exhaust connections under heavy load.

## Bug 6 – bug6.c

**Intended Behavior**: Return the maximum value from an integer array.  
**Issue Type**: Off-by-one error causing out-of-bounds access.  
**Notes**: Loop uses `<=` instead of `<`, leading to undefined behavior.
