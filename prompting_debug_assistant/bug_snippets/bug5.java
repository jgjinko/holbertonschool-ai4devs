// Bug 5 – bug5.java
// ==================
// Type: Misuse of Data Types / Type Mismatch
// Intended Behavior: The executeQuery method should accept integer parameters and properly
//                   format them into the SQL query string (e.g., "SELECT * FROM users WHERE id = 5 AND age = 25").
// Issue: Passing incompatible data types to database methods.
// Notes: The executeQuery method casts an int[] array to Object[], which
//        causes type incompatibility since String.format expects Object[].

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