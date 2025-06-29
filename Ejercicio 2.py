
using System;
using System.Collections.Generic;
using System.Linq;

public class Numeros
{
    private List<int> listaNumeros;

    public Numeros()
    {
        listaNumeros = new List<int>();
        for (int i = 1; i <= 10; i++)
        {
            listaNumeros.Add(i);
        }
    }

    public void MostrarNumerosInversos()
    {
        var numerosInversos = listaNumeros.AsEnumerable().Reverse();
        Console.WriteLine(string.Join(", ", numerosInversos));
    }
}

class Program
{
    static void Main()
    {
        Numeros numeros = new Numeros();
        Console.WriteLine("Números del 1 al 10 en orden inverso:");
        numeros.MostrarNumerosInversos();
    }
}