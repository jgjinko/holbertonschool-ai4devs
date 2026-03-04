// bug2_fixed.js
// Fixed version of bug2.js

// Type: Missing base case leading to infinite recursion (fixed)

function factorial(n) {
    // Added base case to handle zero and negative inputs
    if (n === 0) return 1;
    if (n < 0) throw new Error("Negative input not allowed");
    return n * factorial(n - 1);
}

function main() {
    console.log("Factorial of 5:", factorial(5));
    console.log("Factorial of 0:", factorial(0));
    // console.log("Factorial of -1:", factorial(-1)); // would throw
}

main();
