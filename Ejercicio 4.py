
using System;

class Program
{
    static void Main()
    {
        // Definir la palabra
        string palabra = "psicopedagogía".ToLower();

        // Inicializar contadores para cada vocal
        int a = 0, e = 0, i = 0, o = 0, u = 0;

        // Contar vocales
        foreach (char c in palabra)
        {
            switch (c)
            {
                case 'a':
                    a++;
                    break;
                case 'e':
                    e++;
                    break;
                case 'i':
                    i++;
                    break;
                case 'o':
                    o++;
                    break;
                case 'u':
                    u++;
                    break;
                case 'í':
                    i++;
                    break;
            }
        }

        // Mostrar resultados
        Console.WriteLine("Número de veces que contiene cada vocal:");
        Console.WriteLine($"A: {a}");
        Console.WriteLine($"E: {e}");
        Console.WriteLine($"I: {i}");
        Console.WriteLine($"O: {o}");
        Console.WriteLine($"U: {u}");
    }
}
