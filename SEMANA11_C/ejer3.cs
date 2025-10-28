using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA11_C
{
  internal class ejer3
  {
    static void Main(string[] args)
    {
      int[] num = new int[6];
      num[0] = 10;
      num[1] = 50;
      num[2] = 6;
      num[3] = 3;
      num[4] = 7;
      num[5] = 20;

      int minimo = num[0];
      int maximo = num[0];

      for(int i = 1; i < num.Length; i++)
      {
        if(num[i] < minimo)
          minimo = num[i];
        if(num[i] > maximo)
          maximo = num[i];
      }
      Console.WriteLine("Máximo: " + maximo);
      Console.WriteLine("Mínimo: "+minimo);
    }
  }
}
