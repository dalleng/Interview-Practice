
/* Reverse a string in place */

public class Main {
    public static void main(String[] args) {
        char[] aString = "hola".toCharArray();
        strrev(aString);
        System.out.println(aString);
    }

    public static void strrev(char[] string) {
        int front = 0;
        int back = string.length - 1;
        //char aux;
        
        while (front < back) {
            /* 
             * Swapping with an aux variable
             * aux = string[front];
             * string[front] = string[back];
             * string[back] = aux;
            */

            // xor swapping
            string[front] ^= string[back];
            string[back] ^= string[front];
            string[front] ^= string[back];
            front++;
            back--;
        }
    }
}
