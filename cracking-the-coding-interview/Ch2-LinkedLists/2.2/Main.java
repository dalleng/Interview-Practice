import java.lang.StringBuilder;

public class Main {
    public static void main(String[] args) {
        LinkedList l = new LinkedList();

        l.addLast(1);
        l.addLast(1);
        l.addLast(2);
        l.addLast(3);
        l.addLast(3);
        l.addLast(3);
        l.addLast(3);
        l.addLast(3);
        l.addLast(3);
        l.addLast(4);
        l.addLast(3);
        l.addLast(4);
        l.addLast(2);

        // Prints 1 -> 1 -> 2 -> 3 -> 3 -> 3 -> 3 -> 3 -> 3 -> 4 -> 3 -> 4 -> 2
        System.out.println(l);

        l.removeDuplicates();

        // Prints 1 -> 2 -> 3 -> 4
        System.out.println(l);
    }
}

class Node {
    private int data;
    private Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }

    public Node getNext() {
        return this.next;
    }

    public void setNext(Node n) {
        this.next = n;
    }

    public int getData() {
        return this.data;
    }

    public void setData(int data) {
        this.data = data;
    }

}

class LinkedList {
    Node root = null;
    Node tail = null;

    LinkedList() {
    }

    public void addFirst(int data) {
        if (root == null) {
            addFirstElement(data);
        } else {
            Node n = new Node(data);
            n.setNext(root);
            root = n;
        }
    }

    public void addLast(int data) {
        if (root == null) {
            addFirstElement(data);
        } else {
            Node n = new Node(data);
            this.tail.setNext(n);
            this.tail = n;
        }
    }

    private void addFirstElement(int data) {
        this.root = new Node(data);
        this.tail = this.root;
    }

    public boolean isEmpty() {
        return root == null;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node current = this.root;

        while (current != null) {
            if (current.getNext() != null) {
                sb.append(current.getData() + " -> ");
            } else {
                sb.append(current.getData());
            }
            current = current.getNext();
        }

        return sb.toString();
    }
}
