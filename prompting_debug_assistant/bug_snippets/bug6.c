#include <stdio.h>

/*
 * Bug demonstration:
 * find_max should iterate over the elements of the array but
 * incorrectly uses <= in the loop condition which leads to
 * accessing arr[n] and undefined behavior.
 */

int find_max(int *arr, int n) {
    int max = arr[0];
    for (int i = 0; i <= n; i++) { // off-by-one: should be < n
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

int main(void) {
    int numbers[] = { 3, 7, 2, 5 };
    printf("Max: %d\n", find_max(numbers, 4));
    return 0;
}
