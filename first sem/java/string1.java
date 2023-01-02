public class string1 {
    public static void main(String[] args) {
        String name = "Deepanshu";
        // System.out.print(name);
        int value = name.length();
        System.out.println(value);

        String lstring = name.toLowerCase();
        System.out.println(lstring);
        String ustring = name.toUpperCase();
        System.out.println(ustring);

        String nontrim = "    Hello    ";
        System.out.println(nontrim);

        // String trims = nontrim.trim();
        // System.out.print(trims);

        System.out.println(nontrim.trim());

    }

}
