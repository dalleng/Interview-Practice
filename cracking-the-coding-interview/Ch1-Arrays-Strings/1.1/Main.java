import java.util.HashSet;

/*
 * 1.1 Implement an algorithm to determine if a string has all unique characters 
 * What if you can not use additional data structures?
 */

public class Main {
    public static void main(String[] args) {
        System.out.println("uniqueCharacters:");
        System.out.println("String: '" + args[0] + "' are all characters unique? " + uniqueCharacters(args[0]));

        System.out.println("uniqueCharacters2:");
        System.out.println("String: '" + args[0] + "' are all characters unique? " + uniqueCharacters2(args[0]));
    }

    /* 
     * Only handles ascii, does not take into consideration case sensitiviness
     * or whitespace. Basically the same solution listed in the book.
     */
    public static boolean uniqueCharacters(String s) {
        boolean[] seen = new boolean[256];

        for (char i : s.toCharArray()) {
            if (seen[i]) { 
                return false;
            } else {
                seen[i] = true;
            }
        }

        return true;
    }

    /*
     * uniqueCharacters2 handles more than ascii, considers whitespace and case sensitiveness
     * but it uses an extra data structure (HashSet).
     */

    public static boolean uniqueCharacters2(String s) {
        return uniqueCharacters2(s, false, true);
    }

    public static boolean uniqueCharacters2(String s, boolean caseSensitive, boolean ignoreWhitespace) {
        boolean unique = true;
        HashSet<Character> seen = new HashSet<Character>();

        if (ignoreWhitespace) {
            s = s.replaceAll("\\s", "");
        }

        if (!caseSensitive) {
            s = s.toLowerCase();
        }

        for (char i : s.toCharArray()) {
            unique = seen.add(i);
            if (!unique) {
                break;
            }
        }

        return unique;
    }

}
