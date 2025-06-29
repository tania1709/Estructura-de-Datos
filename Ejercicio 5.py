using System;
using System.Linq;

class Program
{
    static void Main()
    {
        // Crear una lista con precios
        var precios = new[] { 50, 75, 46, 22, 80, 65, 8 };

        // Encontrar el menor y el mayor precio
        var menorPrecio = precios.Min();
        var mayorPrecio = precios.Max();

        // Mostrar resultados
        Console.WriteLine("Precios:");
        Console.WriteLine(string.Join(", ", precios));
        Console.WriteLine($"Menor precio: {menorPrecio}");
        Console.WriteLine($"Mayor precio: {mayorPrecio}");
    }
}
