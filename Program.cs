using System;

public class Persona
{
    public string Id { get; set; }
    public string Nombres { get; set; }
    public string Apellidos { get; set; }
    public string Direccion { get; set; }
    public string[] Telefonos { get; set; }

    public Persona(string id, string nombres, string apellidos, string direccion, string[] telefonos)
    {
        Id = id;
        Nombres = nombres;
        Apellidos = apellidos;
        Direccion = direccion;
        Telefonos = telefonos;
    }

    public void MostrarDatos()
    {
        Console.WriteLine($"ID: {Id}");
        Console.WriteLine($"Nombres: {Nombres}");
        Console.WriteLine($"Apellidos: {Apellidos}");
        Console.WriteLine($"Dirección: {Direccion}");
        Console.WriteLine("Teléfonos:");
        foreach (var telefono in Telefonos)
        {
            Console.WriteLine($"- {telefono}");
        }
    }
}

class Program
{
    static void Main()
    {
        string[] telefonos = new string[] { "062923868", "0981664989", "0939124964" };
        Persona persona = new Persona("105010029-4", "Tania Gabriela", "Guamán Guambiango", "Otavalo Cardón Bajo", telefonos);
        persona.MostrarDatos();
    }
}