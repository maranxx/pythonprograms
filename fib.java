import java.util.Scanner;
class Fibonacciseries {
    public static void main(String[] args)
    {
         int FirstTerm=0;
         int SecondTerm=1;
         Scanner obj =new Scanner(System.in);
         System.out.print("Enter total no of elements till the series want to continue=");
         int  numberofelements=obj.nextInt();
         System.out.println("fibonacci series:");
         for(int i=0;i<=numberofelements;i++)
         {
             System.out.print(FirstTerm +",");
             int NextTerm=FirstTerm + SecondTerm;
             FirstTerm=SecondTerm;
             SecondTerm=NextTerm;
         }
    }
}
