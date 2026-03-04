// Bug 2 – bug2.js
// ================
// Type: Missing base case leading to infinite recursion
// Intended Behavior: The factorial function should compute n! correctly and handle edge cases.
//                   factorial(0) should return 1, factorial(5) should return 120.
// Issue: Input of 0 causes a stack overflow due to missing base case.
// Notes: The factorial function lacks a base case check (if n === 0 return 1).
//        Without it, the recursion never terminates and causes a stack overflow.

function factorial(n) {
    // Missing base case: should check if (n === 0) return 1;
    // This causes infinite recursion when n reaches 0 or negative numbers
    return n * factorial(n - 1);
}

function main() {
    console.log("Factorial of 5:", factorial(5));
    // Uncommenting the line below will cause a stack overflow:
    // console.log("Factorial of 0:", factorial(0));
}

main();