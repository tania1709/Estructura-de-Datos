
using System;

public class Circulo
{
    public double Radio { get; set; }

    public Circulo(double radio)
    {
        Radio = radio;
    }

    public double CalcularArea()
    {
        return Math.PI * Math.Pow(Radio, 2);
    }

    public double CalcularPerimetro()
    {
        return 2 * Math.PI * Radio;
    }
}

public class Rectangulo
{
    public double Largo { get; set; }
    public double Ancho { get; set; }

    public Rectangulo(double largo, double ancho)
    {
        Largo = largo;
        Ancho = ancho;
    }

    public double CalcularArea()
    {
        return Largo * Ancho;
    }

    public double CalcularPerimetro()
    {
        return 2 * (Largo + Ancho);
    }
}

class Program
{
    static void Main(string[] args)
    {
        Circulo circulo = new Circulo(5);
        Console.WriteLine("Círculo:");
        Console.WriteLine("Área: " + circulo.CalcularArea());
        Console.WriteLine("Perímetro: " + circulo.CalcularPerimetro());

        Rectangulo rectangulo = new Rectangulo(4, 6);
        Console.WriteLine("\nRectángulo:");
        Console.WriteLine("Área: " + rectangulo.CalcularArea());
        Console.WriteLine("Perímetro: " + rectangulo.CalcularPerimetro());
    }
}
