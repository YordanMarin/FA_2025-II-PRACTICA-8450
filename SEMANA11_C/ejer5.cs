using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA11_C
{
  internal class ejer5
  {
    static void Main(string[] args)
    {
      Console.Write("Ingrese la cantidad de números: ");
      int cant = int.Parse(Console.ReadLine());

      int[] num = new int[cant];
      int suma = 0;

      for (int i = 0; i < cant; i++)
      {
        Console.Write($"Ingrese número {i + 1}: ");
        num[i] = int.Parse(Console.ReadLine());
        suma += num[i];
      }

      Console.Write("\nNúmeros ingresados: ");
      foreach (int i in num)
        Console.Write(i + " ");

      Console.WriteLine("\n\nSuma total: "+suma);
    }
  }
}
