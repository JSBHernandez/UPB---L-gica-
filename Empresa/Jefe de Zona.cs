using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Empresa
{
    class Jefe_de_Zona : Empleado
    {
        //Atributos

        String coche;

        public Jefe_de_Zona(String coche, String nombre, String apellido, int DNI, String direccion, int telefono, double salario, int antiguedad, Empleado supervisor) : 
            base(nombre, apellido, DNI, direccion, telefono, salario, antiguedad, supervisor)
        {
            this.coche = coche;
        }

        Array List<Vendedores> (vendedores= new ArrayList<>());
        Array List<Secretario> (secretarios= new ArrayList<>());
        Array List<Vendedores> (vendedores= new ArrayList<>());

        public void asignarVendedor(Vendedor nuevoVendedor)
        {
            this.vendedores.add(nuevoVendedor);
            nuevoVendedor.cambiar(this);
        }

        public void mostrarVendedor()
        {
            for(int i=0; i < this.vendedores.size(); i++)
            {
                this.secretrario.get(i).imprimir();
            }
        }

        public void DaraltaSecretario(Empleado nuevoSecretario)
        {
            this.supervisor = nuevoSecretario;
            Console.Write("dar de alta " + nuevoSecretario);

        }
        public void DarbajaSecretario(Empleado nuevoSecretario)
        {
            this.supervisor = nuevoSecretario;
            Console.Write("daeo de baja " + nuevoSecretario);

        }

        public new void Imprimir()
        {
            base.Imprimir();
            Console.Write("El auto asignado es: " + this.coche);
            Console.WriteLine(coche);
        }
    }
}
