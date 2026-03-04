// bug4_fixed.cs
// Fixed version of bug4.cs
using System;
using System.IO;
using System.Linq;
class Program
{
    static int CountWordsInFile(string filePath)
    {
        if (!File.Exists(filePath))
            throw new FileNotFoundException("File not found", filePath);

        string[] lines = File.ReadAllLines(filePath);
        if (lines == null || lines.Length == 0)
            return 0; // empty file has zero words

        int wordCount = 0;
        foreach (string line in lines)
        {
            if (string.IsNullOrWhiteSpace(line))
                continue;
            // use RemoveEmptyEntries to avoid counting extra spaces
            wordCount += line.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries).Length;
        }
        return wordCount;
    }
    static void Main()
    {
        string filePath = "input.txt";
        try
        {
            int words = CountWordsInFile(filePath);
            Console.WriteLine("Total words: " + words);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}