import java.util.Scanner;

public class string {
    public static void main(String[] args) {
        // String name = new String(original:"Hello");
        // String name = "Deepanshu":
        // System.out.println(name);
        int a = 6;
        float b = 5.66f;
        System.out.printf("the value of a is %d and value of b is %f\n", a, b);
        Scanner sc = new Scanner(System.in);
        // string st = sc.next();
        System.out.print("enter the stiring: ");
        String st = sc.nextLine();
        System.out.println(st);
        sc.close();
    }
}