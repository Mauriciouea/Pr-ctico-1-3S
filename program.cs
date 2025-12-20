using System;
using System.Collections.Generic;

namespace ClinicaSaludIntegral
{
    // ================= CLASE PACIENTE =================
    public class Paciente
    {
        public string Cedula { get; set; }
        public string Nombre { get; set; }
        public string Apellido { get; set; }
        public int Edad { get; set; }
        public string Telefono { get; set; }
        public string Email { get; set; }
        public List<Turno> HistorialTurnos { get; set; }

        public Paciente(string cedula, string nombre, string apellido, int edad, string telefono, string email)
        {
            Cedula = cedula;
            Nombre = nombre;
            Apellido = apellido;
            Edad = edad;
            Telefono = telefono;
            Email = email;
            HistorialTurnos = new List<Turno>();
        }

        public string ObtenerNombreCompleto()
        {
            return $"{Nombre} {Apellido}";
        }

        public void AgregarTurno(Turno turno)
        {
            HistorialTurnos.Add(turno);
        }
    }

    // ================= CLASE DOCTOR =================
    public class Doctor
    {
        public string IdDoctor { get; set; }
        public string Nombre { get; set; }
        public string Apellido { get; set; }
        public string Especialidad { get; set; }
        public string Telefono { get; set; }
        public List<DateTime> HorariosDisponibles { get; set; }

        public Doctor(string id, string nombre, string apellido, string especialidad, string telefono)
        {
            IdDoctor = id;
            Nombre = nombre;
            Apellido = apellido;
            Especialidad = especialidad;
            Telefono = telefono;
            HorariosDisponibles = new List<DateTime>();
        }

        public string ObtenerNombreCompleto()
        {
            return $"Dr. {Nombre} {Apellido}";
        }
    }

    // ================= CLASE TURNO =================
    public class Turno
    {
        public string IdTurno { get; set; }
        public Paciente Paciente { get; set; }
        public Doctor Doctor { get; set; }
        public DateTime FechaHora { get; set; }
        public string Motivo { get; set; }
        public string Estado { get; set; }
        public string Observaciones { get; set; }

        public static readonly List<string> EstadosValidos =
            new List<string> { "PENDIENTE", "CONFIRMADO", "CANCELADO", "ATENDIDO" };

        public Turno(string id, Paciente paciente, Doctor doctor, DateTime fechaHora, string motivo)
        {
            IdTurno = id;
            Paciente = paciente;
            Doctor = doctor;
            FechaHora = fechaHora;
            Motivo = motivo;
            Estado = "PENDIENTE";
            Observaciones = "";
        }

        public bool CambiarEstado(string nuevoEstado)
        {
            if (EstadosValidos.Contains(nuevoEstado))
            {
                Estado = nuevoEstado;
                return true;
            }
            return false;
        }
    }

    // ================= SISTEMA PRINCIPAL =================
    public class SistemaTurnosClinica
    {
        private List<Paciente> pacientes = new List<Paciente>();
        private List<Doctor> doctores = new List<Doctor>();
        private List<Turno> turnos = new List<Turno>();
        private int contadorTurnos = 1;

        public SistemaTurnosClinica()
        {
            InicializarDatos();
        }

        private void InicializarDatos()
        {
            doctores.Add(new Doctor("D001", "Carlos", "Mendoza", "Cardiología", "0991234567"));
            doctores.Add(new Doctor("D002", "Ana", "García", "Pediatría", "0992345678"));

            pacientes.Add(new Paciente("1723456789", "María", "Pérez", 35, "0991112233", "maria@email.com"));

            DateTime baseFecha = DateTime.Now.Date.AddHours(9);
            foreach (var doctor in doctores)
            {
                for (int i = 0; i < 4; i++)
                {
                    doctor.HorariosDisponibles.Add(baseFecha.AddHours(i * 2));
                }
            }
        }

        public void Ejecutar()
        {
            Console.WriteLine("Sistema de Gestión de Turnos - Clínica Salud Integral");
            Console.WriteLine("Pacientes registrados: " + pacientes.Count);
            Console.WriteLine("Doctores disponibles: " + doctores.Count);
        }
    }

    // ================= PROGRAMA =================
    class Program
    {
        static void Main(string[] args)
        {
            SistemaTurnosClinica sistema = new SistemaTurnosClinica();
            sistema.Ejecutar();
            Console.ReadKey();
        }
    }
}
