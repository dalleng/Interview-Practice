import java.lang.StringBuilder;

/*
 * 3.1 Describe how you could use a single array to implement three stacks.
 */

public class Main {
    public static void main(String[] args) {
        TriStack ts = new TriStack(5);
        int i;

        System.out.println(ts);

        for (i = 0; i < 5; i++) {
            ts.push(i, 1);
        }
        // should not add anything
        ts.push(i, 1);

        System.out.println(ts);

        for (i = 0; i < 5; i++) {
            System.out.println(ts.pop(1));
        }
        // does not decrement top
        ts.pop(1); 

        System.out.println(ts);
    }
}

class TriStack {
    private Integer[] stacks;
    private int top1;
    private int top2;
    private int top3;

    TriStack(int partitionSize) {
        this.stacks = new Integer[partitionSize * 3];
        this.top1 = 0;
        this.top2 = stacks.length / 3;
        this.top3 = 2 * stacks.length / 3;
    }

    public void push(int data, int stackNumber) {
        if (stackNumber < 1 || stackNumber > 3) {
            return;
        }

        Integer top = null;
        Integer limit = null;

        switch (stackNumber) {
            case 1:
                limit = stacks.length / 3 - 1;
                top = top1;
                break;
            case 2:
                 limit = 2 * stacks.length / 3 - 1;
                 top = top2;
                break;
            case 3:
                limit = stacks.length - 1;
                top = top3;
                break;
        }

        if (top <= limit) {
            stacks[top] = data;
            incrementTop(stackNumber);
        }
    }

    public Integer pop(int stackNumber) {
        Integer retVal = null;
        Integer limit = null;
        Integer top = null;

        switch (stackNumber) {
            case 1:
                limit = 0;
                top = top1;
                break;
            case 2:
                limit = stacks.length / 3;
                top = top2;
                break;
            case 3:
                limit = 2 * stacks.length / 3;
                top = top3;
                break;
        }

        if (top - 1 >= limit) {
            retVal = stacks[top - 1];
            stacks[top - 1] = null;
            incrementTop(stackNumber, -1);
        }

        return retVal;
    }

    private void incrementTop(int stackNumber) {
        incrementTop(stackNumber, 1);
    }

    private void incrementTop(int stackNumber, int n) {
        switch (stackNumber) {
            case 1:
                top1 += n;
                break;
            case 2:
                top2 += n;
                break;
            case 3:
                top3 += n;
                break;
        }
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("top1: " + this.top1 + " top2: " + this.top2 + " top3: " + this.top3 + "\n");

        for (int i = 0; i < stacks.length; i++) {
            sb.append(this.stacks[i] + " ");

            // fugly conditional
            if (i == stacks.length / 3 - 1 || i == 2 * stacks.length / 3 -1 || i == stacks.length - 1) {
                sb.append("\n");
            }
        }
        
        return sb.toString();
    }
}
