// bug3.cpp
// Type: Runtime Exception

#include <iostream>
using namespace std;

double divideNumbers(int a, int b) {
    return a / b;
}

int main() {
    int num1, num2;

    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    double result = divideNumbers(num1, num2);

    cout << "Result: " << result << endl;

    return 0;
}