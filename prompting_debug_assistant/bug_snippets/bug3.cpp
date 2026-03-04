// bug3.cpp
// Type: Incorrect pivot selection causing poor performance
// Intended Behavior: Sort an array of integers using quicksort.
// Issue: Worst-case O(n²) behavior on already sorted arrays.
#include <iostream>
using namespace std;
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // Bug: Always selecting the first element as pivot
        // This causes O(n²) behavior on sorted arrays
        int pivot = arr[low];
        int i = low + 1;
        int j = high;
        while (i <= j) {
            while (i <= j && arr[i] <= pivot) i++;
            while (i <= j && arr[j] > pivot) j--;
            if (i < j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }    
        int temp = arr[low];
        arr[low] = arr[j];
        arr[j] = temp;
        quickSort(arr, low, j - 1);
        quickSort(arr, j + 1, high);
    }
}
int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int n = 5;
    quickSort(numbers, 0, n - 1); 
    for (int i = 0; i < n; i++) {
        cout << numbers[i] << " ";
    }
    cout << endl; 
    return 0;
}