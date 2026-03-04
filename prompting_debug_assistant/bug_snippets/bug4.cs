// bug4.cs
// Type: Off-by-One Error

using System;

class Program
{
    static void PrintElements(string[] items)
    {
        for (int i = 0; i <= items.Length; i++)
        {
            Console.WriteLine("Item: " + items[i]);
        }
    }

    static void Main()
    {
        string[] fruits = { "Apple", "Banana", "Cherry" };
        PrintElements(fruits);
    }
}