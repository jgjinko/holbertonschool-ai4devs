// bug3_fixed.cpp
// Fixed version of bug3.cpp
// Type: Incorrect pivot selection causing poor performance
// Fix: Use median-of-three pivot selection to avoid worst-case behavior.
#include <iostream>
#include <cstdlib>
using namespace std;
int medianOfThree(int arr[], int a, int b, int c) {
    int x = arr[a], y = arr[b], z = arr[c];
    if ((x <= y && y <= z) || (z <= y && y <= x)) return b;
    if ((y <= x && x <= z) || (z <= x && x <= y)) return a;
    return c;
}
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // choose pivot using median-of-three to improve performance
        int pivotIndex = medianOfThree(arr, low, (low+high)/2, high);
        int pivot = arr[pivotIndex];
        // swap pivot to start
        swap(arr[pivotIndex], arr[low]);
        int i = low + 1;
        int j = high;
        while (i <= j) {
            while (i <= j && arr[i] <= pivot) i++;
            while (i <= j && arr[j] > pivot) j--;
            if (i < j) {
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[low], arr[j]);
        quickSort(arr, low, j - 1);
        quickSort(arr, j + 1, high);}}int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int n = 5;
    quickSort(numbers, 0, n - 1);
    for (int i = 0; i < n; i++) cout << numbers[i] << " ";
    cout << endl;
    return 0;
}