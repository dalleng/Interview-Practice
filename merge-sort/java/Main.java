import java.util.Arrays;
import java.util.Random;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        // Test my merge sort implementation by sorting
        // a randon array of integers
        int[] someIntegers = randomIntegerArray();

        Arrays.sort(someIntegers);

        boolean equals = Arrays.equals(mergeSort(someIntegers), someIntegers);
        System.out.println(equals);
    }

    public static int[] randomIntegerArray() {
        Random generator = new Random();
        int randomSize = generator.nextInt(100) + 1;
        int[] randomArray = new int[randomSize];

        for (int i = 0; i < randomSize; i++) {
            randomArray[i] = generator.nextInt();
        }

        return randomArray;
    }

    public static int[] mergeSort(int[] a) {
        if (a.length <= 1) {
            return a;
        } else {
            int[] firstHalf = Arrays.copyOfRange(a, 0, a.length / 2);
            firstHalf = mergeSort(firstHalf);

            int[] secondHalf = Arrays.copyOfRange(a, a.length / 2, a.length);
            secondHalf = mergeSort(secondHalf);

            return merge(firstHalf, secondHalf);
        }
    }

    public static int[] merge(int[] a, int[] b) {
        int size = a.length + b.length;
        int[] merged = new int[size];

        int j = 0;
        int k = 0; 

        for (int i = 0; i < size; i++) {
            if (j > a.length - 1) {
                merged[i] = b[k];
                k++;
            } else if (k > b.length - 1) {
                merged[i] = a[j];
                j++;
            } else if (a[j] < b[k]) {
                merged[i] = a[j];
                j++;
            } else {
                merged[i] = b[k];
                k++;
            }
        }
        
        return merged;
    }
}
