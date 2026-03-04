// bug2.js
// Type: Logical Error

function calculateAverage(numbers) {
    let total = 0;

    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }

    // Logical mistake: dividing by 2 instead of numbers.length
    let average = total / 2;

    return average;
}

function main() {
    const grades = [80, 90, 100, 70];
    const avg = calculateAverage(grades);
    console.log("Average grade:", avg);
}

main();