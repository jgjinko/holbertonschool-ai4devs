// bug5_fixed.java
// Fixed version of bug5.java

import java.sql.*;
import java.util.Arrays;

public class bug5_fixed {

    public static void executeQuery(String query, int[] params) {
        try {
            // Convert primitive ints to Integer objects before formatting
            Object[] boxed = Arrays.stream(params).boxed().toArray();
            String sql = String.format(query, boxed);
            System.out.println("Executing: " + sql);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        String query = "SELECT * FROM users WHERE id = %s AND age = %s";
        int[] parameters = {5, 25};
        executeQuery(query, parameters);
    }
}
