using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Empresa
{
    class Empleado
    {
        //Atributos

        String nombre;
        String apellido;
        int DNI;
        String direccion;
        int telefono;
        double salario;
        int antiguedad;
        Empleado supervisor;

        // COnstructor

        public Empleado(String nombre, String apellido, int DNI, String direccion, int telefono, double salario, int antiguedad, Empleado supervisor)
        {
            this.nombre = nombre;
            this.apellido = apellido;
            this.DNI = DNI;
            this.direccion = direccion;
            this.telefono = telefono;
            this.salario = salario;
            this.antiguedad = antiguedad;
            this.supervisor = supervisor;
        }

        public void Imprimir()
        {
            Console.Write("nombre" + nombre);
            Console.WriteLine(nombre);
            Console.Write("apellido" + apellido);
            Console.WriteLine(apellido);
            Console.Write("DNI" + DNI);
            Console.WriteLine(DNI);
            Console.Write("direccion" + direccion);
            Console.WriteLine(direccion);
            Console.Write("telefono" + telefono);
            Console.WriteLine(telefono);
            Console.Write("salario" + salario);
            Console.WriteLine(salario);
            Console.Write("antiguedad" + antiguedad);
            Console.WriteLine(antiguedad);    
        }

        public void cambiar (Empleado nuevosupervisor)
        {
            supervisor = nuevosupervisor;
        }

        public void incrementar (double incremento)
        {
            salario = salario + incremento * salario;
            Console.Write("El sueldo del empleado con el aumento es de" + salario);
            Console.WriteLine(salario);
        }
    }
}
