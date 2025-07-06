using System;

public class Nodo
{
    public int Valor { get; set; }
    public Nodo Siguiente { get; set; }

    public Nodo(int valor)
    {
        Valor = valor;
        Siguiente = null;
    }
}

public class ListaEnlazada
{
    public Nodo Cabeza { get; set; }

    public ListaEnlazada()
    {
        Cabeza = null;
    }

    public void AgregarNodo(int valor)
    {
        Nodo nuevoNodo = new Nodo(valor);

        if (Cabeza == null)
        {
            Cabeza = nuevoNodo;
        }
        else
        {
            Nodo actual = Cabeza;
            while (actual.Siguiente != null)
            {
                actual = actual.Siguiente;
            }
            actual.Siguiente = nuevoNodo;
        }
    }

    public void EliminarNodosFueraDeRango(int min, int max)
    {
        if (Cabeza == null) return;

        // Eliminar nodos al principio de la lista
        while (Cabeza != null && (Cabeza.Valor < min || Cabeza.Valor > max))
        {
            Cabeza = Cabeza.Siguiente;
        }

        Nodo actual = Cabeza;
        while (actual != null && actual.Siguiente != null)
        {
            if (actual.Siguiente.Valor < min || actual.Siguiente.Valor > max)
            {
                actual.Siguiente = actual.Siguiente.Siguiente;
            }
            else
            {
                actual = actual.Siguiente;
            }
        }
    }

    public void ImprimirLista()
    {
        Nodo actual = Cabeza;
        while (actual != null)
        {
            Console.Write(actual.Valor + " ");
            actual = actual.Siguiente;
        }
        Console.WriteLine();
    }
}

class Program
{
    static void Main(string[] args)
    {
        ListaEnlazada lista = new ListaEnlazada();
        Random random = new Random();

        // Agregar 50 nodos aleatorios a la lista
        for (int i = 0; i < 50; i++)
        {
            lista.AgregarNodo(random.Next(1, 1000));
        }

        Console.WriteLine("Lista original:");
        lista.ImprimirLista();

        // Leer rango de valores desde el teclado
        Console.Write("Ingrese el valor mínimo del rango: ");
        int min = Convert.ToInt32(Console.ReadLine());
        Console.Write("Ingrese el valor máximo del rango: ");
        int max = Convert.ToInt32(Console.ReadLine());

        // Eliminar nodos fuera del rango
        lista.EliminarNodosFueraDeRango(min, max);

        Console.WriteLine("Lista después de eliminar nodos fuera del rango:");
        lista.ImprimirLista();
    }
}