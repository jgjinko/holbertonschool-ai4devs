// Bug 4 – bug4.cs
// ================
// Type: Null reference when file is empty
// Intended Behavior: Read lines from a file and count words.
// Issue: Does not handle empty or missing files gracefully.
// Notes: File.ReadAllLines returns an empty array (not null) for empty files,
//        but the code does not validate this condition, leading to incorrect counts.
using System;
using System.IO;
using System.Linq;
class Program
{
    static int CountWordsInFile(string filePath)
    {
        // Bug: Does not check if file is empty or null
        // This causes a NullReferenceException when file is empty
        string[] lines = File.ReadAllLines(filePath);
        
        int wordCount = 0;
        foreach (string line in lines)
        {
            // Null reference exception occurs here if lines is null or empty
            wordCount += line.Split(' ').Length;
        }
        
        return wordCount;
    }
    static void Main()
    {string filePath = "input.txt";
        try
        {int words = CountWordsInFile(filePath);
            Console.WriteLine("Total words: " + words);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}