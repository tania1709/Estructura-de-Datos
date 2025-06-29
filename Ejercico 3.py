
using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        // Crear una lista con el abecedario
        var abecedario = Enumerable.Range('A', 26).Select(i => (char)i).ToList();

        // Eliminar letras en posiciones múltiplos de 3
        for (int i = abecedario.Count - 1; i >= 0; i--)
        {
            if ((i + 1) % 3 == 0)
            {
                abecedario.RemoveAt(i);
            }
        }

        // Mostrar la lista resultante
        Console.WriteLine("Abecedario sin letras en posiciones múltiplos de 3:");
        Console.WriteLine(string.Join(", ", abecedario));
    }
}

