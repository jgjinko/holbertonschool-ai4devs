## Bug 1 – bug1.py

**Type:** Off-by-one error

**Intended Behavior:**  
When n equals the list length, the function should return all items intact. For example, `get_last_n_items([1,2,3,4,5], 5)` should return `[1,2,3,4,5]`. When n is less than the list length, it should return only the last n items (e.g., `get_last_n_items([1,2,3,4,5], 2)` returns `[4,5]`).

**Issue:**  
The function fails when n == len(items) due to incorrect slicing. The start_index calculation subtracts one too many, causing the function to skip the first item when n equals the list length.

**Notes:**  
The bug occurs in the line `start_index = len(items) - n - 1`. It should be `start_index = len(items) - n` to properly calculate the starting position for the last n items.

---

## Bug 2 – bug2.js

**Type:** Missing base case leading to infinite recursion

**Intended Behavior:**  
The factorial function should compute n! correctly and handle edge cases properly. `factorial(0)` should return `1`, `factorial(5)` should return `120`, and the function should work for all non-negative integers without causing a stack overflow.

**Issue:**  
Input of 0 causes a stack overflow due to missing base case. The factorial function lacks a base case check, so it continues recursing indefinitely.

**Notes:**  
The function is missing the base case `if (n === 0) return 1;` at the beginning. Without it, when n reaches 0 or negative numbers, the recursion never terminates and causes a stack overflow error.

---

## Bug 3 – bug3.cpp

**Type:** Incorrect pivot selection causing poor performance

**Intended Behavior:**  
The quicksort function should efficiently sort arrays in O(n log n) average time complexity, even when the input is already sorted. For example, sorting `[1, 2, 3, 4, 5]` should complete in reasonable time without degradation.

**Issue:**  
Worst-case O(n²) behavior on already sorted arrays. The function always selects the first element as the pivot, which causes poor partitioning on sorted or nearly-sorted data.

**Notes:**  
The bug is in the line `int pivot = arr[low];`. A better approach would be to use a random pivot selection or median-of-three strategy to avoid worst-case performance. The current implementation degrades to O(n²) when the input is already sorted or reverse-sorted.

---

## Bug 4 – bug4.cs

**Type:** Null reference when file is empty

**Intended Behavior:**  
When the input file is empty (contains 0 bytes), the function should return a word count of `0` without throwing an exception. The function should gracefully handle both empty and missing files by returning appropriate error information or default values.

**Issue:**  
The code does not handle empty or missing files gracefully. While `File.ReadAllLines` returns an empty array for empty files (not null), the subsequent loop operation on empty input produces unexpected results.

**Notes:**  
The function should validate that the file exists and contains content before attempting to process it. The current implementation doesn't check if the file is empty before iterating through lines, which can lead to incorrect word counts or exceptions when the file doesn't exist.

---

## Bug 5 – bug5.java

**Type:** Misuse of Data Types / Type Mismatch

**Intended Behavior:**  
The `executeQuery` method should accept integer parameters and properly format them into the SQL query string. For example, with query `"SELECT * FROM users WHERE id = %s AND age = %s"` and parameters `[5, 25]`, the result should be `"SELECT * FROM users WHERE id = 5 AND age = 25"`.

**Issue:**  
Passing incompatible data types to the `String.format` method causes a runtime error. The method casts an `int[]` array to `Object[]`, which is incompatible with `String.format`'s expectations.

**Notes:**  
The bug is in casting `int[] params` to `(Object[]) params`. In Java, primitive arrays cannot be directly cast to Object arrays. The parameters should be boxed (converted to Integer objects) or the method signature should accept `Object[]` which can hold any type of object.

---

## Bug 6 – bug6.c

**Type:** Off-by-one error and buffer overflow

**Intended Behavior:**  
The `find_max` function should iterate through exactly n elements (array indices 0 to n-1) and return the maximum value without accessing memory beyond the array bounds. For the array `[3, 7, 2, 5]` with size 4, it should return `7`.

**Issue:**  
Incorrectly using `<=` in the loop condition causes out-of-bounds access. The loop accesses `arr[n]`, which is beyond the valid array bounds (0 to n-1), resulting in undefined behavior.

**Notes:**  
The bug is in the line `for (int i = 0; i <= n; i++)`. It should be `for (int i = 0; i < n; i++)` to properly iterate within the valid bounds. Accessing `arr[n]` reads undefined memory and can return garbage values or cause a segmentation fault.