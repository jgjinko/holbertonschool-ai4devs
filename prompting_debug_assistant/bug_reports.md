# Bug Reports

## Bug Report – bug1.py
- **Summary**: Off-by-one error in slicing causes the function to skip the first element when returning all items.  
- **Root Cause**: Subtracted an extra index in `items[len(items)-n-1:]` instead of `items[len(items)-n:]`.  
- **Resolution**: Changed the start_index calculation from `len(items) - n - 1` to `len(items) - n`, or use idiomatic Python `items[-n:]`.  
- **Lesson Learned**: Always test edge cases like when n equals the list length; boundary conditions are common sources of off-by-one errors.  

---

## Bug Report – bug2.js
- **Summary**: Missing base case in recursive factorial function causes infinite recursion and stack overflow.  
- **Root Cause**: Function lacks termination condition for `n === 0`, causing recursion to continue indefinitely into negative numbers.  
- **Resolution**: Added base case `if (n === 0) return 1;` at the function entry. Also added input validation for negative inputs.  
- **Lesson Learned**: Every recursive function must have a clearly defined base case; test with boundary inputs (0, 1, negatives).  

---

## Bug Report – bug3.cpp
- **Summary**: Quicksort degrades to O(n²) performance on already sorted or nearly sorted arrays.  
- **Root Cause**: Always selecting the first element as pivot leads to unbalanced partitioning when input is sorted.  
- **Resolution**: Implemented median-of-three pivot selection to improve average performance and avoid worst-case behavior on sorted data.  
- **Lesson Learned**: Pivot selection strategy is critical in quicksort; always consider edge cases (sorted, reverse-sorted, duplicates).  

---

## Bug Report – bug4.cs
- **Summary**: Word counting function fails to handle empty files or null input gracefully, leading to incorrect counts.  
- **Root Cause**: No validation for empty files or null lines before attempting string operations; logic assumes file always has content.  
- **Resolution**: Added file existence check, empty array handling, null/whitespace line filtering, and `StringSplitOptions.RemoveEmptyEntries` for robust splitting.  
- **Lesson Learned**: Always validate file state before processing; use defensive programming with null checks and empty collection handling.  

---

## Bug Report – bug5.java
- **Summary**: Type mismatch when casting primitive int[] to Object[] causes ClassCastException at runtime.  
- **Root Cause**: In Java, primitive arrays cannot be directly cast to Object arrays; the runtime type of int[] is incompatible with Object[].  
- **Resolution**: Convert int[] to Integer[] using `Arrays.stream(params).boxed().toArray()` to properly box primitives before passing to String.format.  
- **Lesson Learned**: Be aware of Java's type system; primitive arrays and object arrays are fundamentally different and require explicit conversion/boxing.  

---

## Bug Report – bug6.c
- **Summary**: Off-by-one error in loop condition causes buffer overflow by accessing memory beyond array bounds.  
- **Root Cause**: Loop condition `i <= n` iterates one too many times, accessing `arr[n]` which is outside the valid range [0, n-1].  
- **Resolution**: Changed loop condition from `i <= n` to `i < n` to ensure iteration only over valid array indices.  
- **Lesson Learned**: Array bounds are always [0, n-1]; off-by-one errors in loop conditions are common and can lead to undefined behavior or crashes.  

---
