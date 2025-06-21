using System;

// Estructura para representar un paciente
public struct Paciente
{
    public string Nombre { get; set; }
    public string Apellido { get; set; }
    public string NSS { get; set; }
    public DateTime FechaNacimiento { get; set; }
}

// Estructura para representar un turno
public struct Turno
{
    public DateTime Fecha { get; set; }
    public TimeSpan Hora { get; set; }
    public string Medico { get; set; }
}

// Clase para representar la Agenda de turnos
public class Agenda
{
    private Paciente[] pacientes;
    private Turno[,] turnos;

    public Agenda(int numPacientes, int numTurnos)
    {
        pacientes = new Paciente[numPacientes];
        turnos = new Turno[numPacientes, numTurnos];
    }

    public void AgregarPaciente(Paciente paciente, int indice)
    {
        pacientes[indice] = paciente;
    }

    public void AgregarTurno(Turno turno, int pacienteIndice, int turnoIndice)
    {
        turnos[pacienteIndice, turnoIndice] = turno;
    }

    public void MostrarAgenda()
    {
        for (int i = 0; i < pacientes.Length; i++)
        {
            Console.WriteLine($"Paciente {i + 1}: {pacientes[i].Nombre} {pacientes[i].Apellido}");
            for (int j = 0; j < turnos.GetLength(1); j++)
            {
                Console.WriteLine($"Turno {j + 1}: {turnos[i, j].Fecha.ToString("dd/MM/yyyy")} {turnos[i, j].Hora}");
            }
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Crear una agenda con 3 pacientes y 2 turnos por paciente
        Agenda agenda = new Agenda(3, 2);

        // Agregar pacientes
        Paciente paciente1 = new Paciente { Nombre = "Jose", Apellido = "Maldonado", NSS = "123456789", FechaNacimiento = DateTime.Parse("1989-07-12") };
        Paciente paciente2 = new Paciente { Nombre = "Gaby", Apellido = "Males", NSS = "987654321", FechaNacimiento = DateTime.Parse("1999-09-03") };
        Paciente paciente3 = new Paciente { Nombre = "Anita", Apellido = "Gualsaqui", NSS = "555555555", FechaNacimiento = DateTime.Parse("2005-03-12") };

        agenda.AgregarPaciente(paciente1, 0);
        agenda.AgregarPaciente(paciente2, 1);
        agenda.AgregarPaciente(paciente3, 2);

        // Agregar turnos
        Turno turno1 = new Turno { Fecha = DateTime.Parse("2025-09-20"), Hora = TimeSpan.Parse("11:00"), Medico = "Dr. Juan" };
        Turno turno2 = new Turno { Fecha = DateTime.Parse("2025-09-20"), Hora = TimeSpan.Parse("12:00"), Medico = "Dra. Carmen" };

        agenda.AgregarTurno(turno1, 0, 0);
        agenda.AgregarTurno(turno2, 0, 1);
        agenda.AgregarTurno(turno1, 1, 0);
        agenda.AgregarTurno(turno2, 1, 1);
        agenda.AgregarTurno(turno1, 2, 0);
        agenda.AgregarTurno(turno2, 2, 1);

        // Mostrar agenda
        agenda.MostrarAgenda();
    }
}