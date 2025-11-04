using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA12
{
    internal class Estudiantes
    {
        byte[] edades = new byte[0];
        int pos = 0;

        public void registrar()
        {
            byte ed;

            while (true)
            {
                Console.Write("\nIngrese edad: ");
                if (byte.TryParse(Console.ReadLine(), out ed) & ed >= 14 && ed <= 120) break;
                else Console.WriteLine("Ingrese una edad correcta!\n");
            }

            Array.Resize(ref edades, edades.Length+1);
            edades[pos] = ed;
            pos++;
            Console.WriteLine("\nEdad registrado correctamente.");
        }

        public void mostrar()
        {
            Console.WriteLine("\nPOS\tEDAD");
            for(int i = 0; i < edades.Length; i++)
            {
                Console.WriteLine(i + "\t" + edades[i]);
            }
        }

        public void eliminar()
        {
            int indice = -1;
            Console.Write("\nIngrese la edad a eliminar: ");
            byte ed = byte.Parse(Console.ReadLine());

            for(int i = 0;i < edades.Length; i++)
            {
                if (edades[i] == ed)
                    indice = i;
            }

            if (indice != -1)
            {
                for(int j=indice; j<edades.Length-1;j++)
                    edades[j] = edades[j+1];

                Array.Resize(ref edades, edades.Length - 1);
                pos--;
                Console.WriteLine("\nEdad eliminado correctamente.");
            }
            else Console.WriteLine("\nNo se puede eliminar porque no existe.");
        }

        public void ordenar()
        {
            for(int i = 0;i < edades.Length-1; i++)
            {
                for(int j =0;j<edades.Length-1-i; j++)
                {
                    if (edades[j] < edades[j + 1])
                    {
                        byte temp = edades[j];
                        edades[j] = edades[j + 1];
                        edades[j + 1] = temp;
                    }
                }
            }
            Console.WriteLine("\nSe ordeno correctamente.");
        }
    }
}
