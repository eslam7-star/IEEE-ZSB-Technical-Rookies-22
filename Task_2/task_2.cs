using System;
using System.Numerics;

namespace printsumofdigits
{
    class Program
    {

        static void Main(string[] args)
        {
            Console.WriteLine("enter your number n : ");
            int n = int.Parse(Console.ReadLine());
            BigInteger[] xarray = new BigInteger[n];
            xarray[0] = 0;
            xarray[1] = 1;
            BigInteger sum = 1;
            for (int x = 2; x <= n - 1; x++)
            {
                xarray[x] = xarray[x - 1] + xarray[x - 2];
            }
            foreach (int c in xarray)
            {
                Console.Write(c + " ");
            }
        }
    }
}
