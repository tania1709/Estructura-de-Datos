using System;
using System.Collections.Generic;

public class Atraccion
{
    private Queue<string> cola;
    private int capacidad;

    public Atraccion(int capacidad = 30)
    {
        this.cola = new Queue<string>();
        this.capacidad = capacidad;
    }

    public void AgregarPersona(string nombre)
    {
        if (cola.Count < capacidad)
        {
            cola.Enqueue(nombre);
            Console.WriteLine($"{nombre} agregado a la cola.");
        }
        else
        {
            Console.WriteLine("La cola está llena. No se pueden agregar más personas.");
        }
    }

    public void SubirAtraccion()
    {
        if (cola.Count > 0)
        {
            string persona = cola.Dequeue();
            Console.WriteLine($"{persona} sube a la atracción.");
        }
        else
        {
            Console.WriteLine("No hay personas en la cola.");
        }
    }

    public void Reporteria()
    {
        Console.WriteLine("Personas en la cola:");
        foreach (var persona in cola)
        {
            Console.WriteLine(persona);
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Atraccion atraccion = new Atraccion();
        for (int i = 1; i <= 35; i++)
        {
            atraccion.AgregarPersona($"Persona {i}");
        }

        atraccion.Reporteria();

        while (atraccion.cola.Count > 0)
        {
            atraccion.SubirAtraccion();
        }
    }
}