import java.util.Scanner;

public class takinginput {
    public static void main(String[] args) {
        System.out.println("Taking a number frem the user");
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Num 1");
        // int a = sc.next();
        float a = sc.nextFloat();
        System.out.println("Enter Num 2");
        // int b = sc.next();
        float b = sc.nextFloat();
        // int sum = a+b;
        float sum = a + b;
        System.out.println("the sum of two number is: ");
        System.out.print(sum);
        boolean b1 = sc.hasNextInt();
        System.out.print(b1);
        System.out.println("Enter the string");
        String str = sc.next();
        String str2 = sc.nextLine();
        System.out.println(str);
        System.out.println(str2);
        sc.close();

    }
}