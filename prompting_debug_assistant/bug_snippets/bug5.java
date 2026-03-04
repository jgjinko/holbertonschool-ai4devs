// bug5.java
// Type: Misuse of Data Types / Type Mismatch
// Intended Behavior: Connect to a database and execute a query.
// Issue: Passing incompatible data types to database methods.

import java.sql.*;

public class bug5 {

    public static void executeQuery(String query, int[] params) {
        try {
            // Bug: params is an int array but the method expects String objects
            // This causes a type mismatch and runtime error
            String sql = String.format(query, (Object[]) params);
            System.out.println("Executing: " + sql);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        String query = "SELECT * FROM users WHERE id = %s AND age = %s";
        int[] parameters = {5, 25};
        
        // This will fail due to type mismatch
        executeQuery(query, parameters);
    }
}