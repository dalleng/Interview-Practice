import java.util.Arrays;
import java.util.ArrayList;

public class MaxHeap {
    private ArrayList<Integer> heap = new ArrayList<Integer>();

    MaxHeap() {
    }
    
    MaxHeap(Integer[] a) {
        this.heap.addAll(Arrays.asList(a));
        buildMaxHeap();
    }

    MaxHeap(int[] a) {
        for (int i : a) {
            this.heap.add(i);
        }
        buildMaxHeap();
    }

    private Integer getParent(int index) {
        int parentIndex = getParentIndex(index);

        if (parentIndex < 0 || parentIndex >= heap.size()) {
            return null;
        } else {
            return heap.get(parentIndex);
        }
    }

    private int getParentIndex(int index) {
        return (index - 1) / 2;
    }

    private Integer getRightChild(int index) {
        int rightChildIndex = getRightChildIndex(index);

        if (rightChildIndex < 0 || rightChildIndex >= heap.size()) {
            return null;
        } else {
            return heap.get(rightChildIndex);
        }
    }

    private Integer getLeftChild(int index) {
        int leftChildIndex = getLeftChildIndex(index);

        if (leftChildIndex < 0 || leftChildIndex > heap.size()) {
            return null;
        } else {
            return heap.get(leftChildIndex);
        }
    }

    private int getRightChildIndex(int index) {
        return 2 * index + 2;
    }

    private int getLeftChildIndex(int index) {
        return 2 * index + 1;
    }

    private void maxHeapify(int index) {
        if (index < 0 || index >= heap.size()) {
            return;
        }
        
        int largestIndex = index;
        int parent = heap.get(index);
        int largest = parent;

        Integer rightChild = getRightChild(index);
        Integer leftChild = getLeftChild(index);

        if (leftChild != null && leftChild > largest) {
            largest = leftChild;
            largestIndex = getLeftChildIndex(index);
        }

        if (rightChild != null && rightChild > largest) {
            largest = rightChild;
            largestIndex = getRightChildIndex(index);
        }

        if (index != largestIndex) {
            swap(index, largestIndex);
            maxHeapify(largestIndex);
        }
    }

    private void swap(int i, int j) {
        Integer aux = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, aux);
    }

    private void buildMaxHeap() {
        for (int i = heap.size() / 2; i >= 0; i--) {
            maxHeapify(i);
        }
    }

    public void insert(int i) {
        this.heap.add(i);
        int index = heap.size() - 1;

        int parentIndex = getParentIndex(index);
        Integer parent = heap.get(parentIndex);

        while (index > 0 && parent < i) {
            swap(index, parentIndex);
            index = parentIndex;
            parentIndex = getParentIndex(index);
            parent = heap.get(parentIndex);
        }
    }

    public Integer extractMax() {
        Integer max = null;

        if (heap.size() > 0) {
            max = heap.get(0);
            heap.remove(0);
            maxHeapify(0);
        }

        return max;
    }

    public int max() {
        return heap.get(0);
    }

    public String toString() {
        return this.heap.toString();
    }

    public static void main(String[] args) {
        Integer[] a = {16, 4, 10, 14, 7, 9, 3, 2, 8, 1};
        MaxHeap mh = new MaxHeap(a);
        System.out.println(mh);
        mh.insert(17);
        mh.insert(16);
        mh.insert(-2);
        mh.insert(4);
        System.out.println(mh.extractMax());
        System.out.println(mh);
    }
}
