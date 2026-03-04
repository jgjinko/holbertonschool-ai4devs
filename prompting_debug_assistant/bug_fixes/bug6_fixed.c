// bug6_fixed.c
// Fixed version of bug6.c

#include <stdio.h>

int find_max(int *arr, int n) {
    int max = arr[0];
    for (int i = 0; i < n; i++) { // corrected condition
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

int main(void) {
    int numbers[] = { 3, 7, 2, 5 };
    int size = 4;
    printf("Max: %d\n", find_max(numbers, size));
    return 0;
}
