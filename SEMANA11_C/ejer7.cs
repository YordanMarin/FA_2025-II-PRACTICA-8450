using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA11_C
{
  internal class ejer7
  {
    static void Main(string[] args)
    {
      Console.Write("Ingrese la cantidad de números: ");
      int cant = int.Parse(Console.ReadLine());

      int[] num = new int[cant];
      Random rnd = new Random();
      Console.WriteLine("\nLista aleatoria:");
      for (int i = 0; i < num.Length; i++)
      {
        num[i] = rnd.Next(1, 51);
        Console.WriteLine(num[i]);
      }
      Console.Write("\nIngrese el número a buscar: ");
      int buscar = int.Parse(Console.ReadLine());

      bool b = false;
      for(int i = 0;i < num.Length; i++)
      {
        if (num[i] == buscar)
        {
          b = true;
        }
      }

      if (b == true)
        Console.WriteLine("Existe");
      else 
        Console.WriteLine("No existe");
    }
  }
}
