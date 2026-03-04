// bug6.c
// Type: Off-by-one error and buffer overflow
// Intended Behavior: Find the maximum element in an array.
// Issue: Incorrectly uses <= in loop condition causing out-of-bounds access.

#include <stdio.h>

int find_max(int *arr, int n) {
    int max = arr[0];
    
    // Bug: Loop condition uses <= instead of <
    // This causes accessing arr[n] which is undefined behavior
    // Should be: for (int i = 0; i < n; i++)
    for (int i = 0; i <= n; i++) {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

int main(void) {
    int numbers[] = { 3, 7, 2, 5 };
    int size = 4;
    
    // The function will access arr[4] which is out of bounds
    printf("Max: %d\n", find_max(numbers, size));
    
    return 0;
}
