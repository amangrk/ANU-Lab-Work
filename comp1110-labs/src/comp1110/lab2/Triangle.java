package comp1110.lab2;

;import java.util.Scanner;

/**
 * Created by Admin on 28-07-2016.
 */
public class Triangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int height=sc.nextInt() ;
        for (int i=1;i<height;i++)
        {
            System.out.print(" ");
        }
        System.out.println("*");
        for (int j=1;j<=height-2;j++)
        {
            for (int k=1;k<=height-j-1;k++)
            {
                System.out.print(" ");
            }
            System.out.print("*");
            for (int l=1;l<=2*j-1;l++)
            {
                System.out.print(" ");
            }
            System.out.println("*");

        }
        if (height>1) {
            for (int m = 0; m < 2 * height - 1; m++) {
                System.out.print("*");
            }
            System.out.println("");

        }

    }
}