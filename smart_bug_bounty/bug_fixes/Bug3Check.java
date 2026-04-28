public class Bug3Check { 
    public static void main(String[] args) { 
        int passed = 0; 
        
        if (bug3.firstUniqueChar("swiss") == "w".charAt(0)) passed++; 
        if (bug3.firstUniqueChar("aabbcc") == '\0') passed++; 
        if (bug3.firstUniqueChar("") == '\0') passed++; 
        
        System.out.println("bug3.java: " + passed + "/3 passed"); 
    }
}