// bug5.java
// Type: Misuse of Data Types

public class bug5 {

    public static double calculateSquareRoot(String value) {
        // Incorrectly passing String directly to Math.sqrt
        return Math.sqrt(value);
    }

    public static void main(String[] args) {
        String number = "25";
        double result = calculateSquareRoot(number);
        System.out.println("Square root: " + result);
    }
}