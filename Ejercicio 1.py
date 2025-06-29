using System;

class Program
{
    static void Main()
    {
        // Definir la lista de asignaturas
        string[] asignaturas = { "Ciencias Naturales", "Filosofía", "Educación Física", "Informática", "Lengua" };

        // Mostrar la lista de asignaturas por pantalla
        Console.WriteLine("Asignaturas del curso:");
        for (int i = 0; i < asignaturas.Length; i++)
        {
            Console.WriteLine($"{i + 1}. {asignaturas[i]}");
        }
    }
}