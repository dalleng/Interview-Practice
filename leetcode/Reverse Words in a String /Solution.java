import java.lang.StringBuilder;

/* Reverse Words in a String
 * https://oj.leetcode.com/problems/reverse-words-in-a-string/
 */

public class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().replaceAll("\\s+", " ").split(" ");
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < words.length; i++) {
            sb.append(words[words.length - 1 - i] + " ");
        }
        
        sb.setLength(sb.length() - 1);
        return sb.toString();
    }
}
