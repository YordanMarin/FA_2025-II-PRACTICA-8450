using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA11_C
{
  internal class ejer6
  {
    static void Main(string[] args)
    {
      string[] productos = new string[5];
      int registro = 0;

      for(int i = 0; registro < productos.Length; i++)
      {
        Console.Write("Ingrese producto: ");
        string pro = Console.ReadLine();
        bool rep = false;

        for(int j = 0; j < productos.Length; j++)
        {
          if(productos[j] == pro)
          {
            Console.WriteLine("Producto ya existente.\n");
            rep = true;
            break;
          }
        }

        if (rep == false)
        {
          productos[registro] = pro;
          registro++;
        }
      }

      Console.WriteLine("\nLista de productos: ");
      foreach (string i in productos)
        Console.WriteLine(i);
    }
  }
}
