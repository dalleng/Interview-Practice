import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        String a = args[0];
        String b = args[1];
        System.out.println("String 1: " + a);
        System.out.println("String 2: " + b);
        System.out.println("Are they anagrams? " + isAnagram(a, b));
    }

    public static HashMap<Character, Integer> getCharacterCount(String s) {
        HashMap<Character, Integer> counter = new HashMap<Character, Integer>();

        for (char i : s.toCharArray()) {
            if (!Character.toString(i).matches("\\s")) {
                if (counter.containsKey(i)) {
                    int count = counter.get(i) + 1;
                    counter.put(i, count);
                } else {
                    counter.put(i, 1);
                }
            }
        }

        return counter;
    }

    public static boolean isAnagram(String a, String b) {
        HashMap<Character, Integer> counterA = getCharacterCount(a);
        HashMap<Character, Integer> counterB = getCharacterCount(b);
        return counterA.equals(counterB);
    }
}
