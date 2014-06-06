/* 
 * 2.2 Implement an algorithm to find the nth to last element of a singly linked list.
 */

public class Main {
	public static void main(String[] args) {
		LinkedList l = new LinkedList();

		l.addLast(1);
		l.addLast(2);
		l.addLast(3);
		l.addLast(4);
		l.addLast(5);
		l.addLast(6);

         System.out.println(l);
         Node n = l.getNthFromEnd(6);
         System.out.println(n);
        
         //l.removeNthFromEnd(-1);
         //System.out.println(l);
        
         //l.removeNthFromEnd(1);
         //System.out.println(l);

		//l.removeNthFromEnd(5);
		//System.out.println(l);

		//l.removeNthFromEnd(2);
		//System.out.println(l);
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

	public String toString() {
		return Integer.toString(this.data);
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

	public void removeNthFromEnd(int n) {
		int count = 0;
		Node node = root;

		if (n <= 0)
			return;

		// count the number of elements
		while (node != null) {
			node = node.getNext();
			count++;
		}

		// fail silently
		if (n > count)
			return;

		Node previous = root;
		Node current, ahead;

		for (int i = 1; i < count - n; i++) {
			previous = previous.getNext();
		}

		if (previous != root) {
            ahead = previous.getNext().getNext();
            previous.setNext(ahead);
        } else {
            root = root.getNext();
        }
	}

    /* Implemented removeNthFromEnd first as I thought that
     * was the question, after re-reading I've noticed the question
     * was about just getting the element. So I modified getNthFromEnd
     * for that purspose.
     */
	public Node getNthFromEnd(int n) {
		int count = 0;
		Node node = root;

		if (n <= 0)
			return null;

		// count the number of elements
		while (node != null) {
			node = node.getNext();
			count++;
		}

		// fail silently
		if (n > count)
			return null;

		Node current = root;

		for (int i = 0; i < count - n; i++) {
			current = current.getNext();
		}

        return current;
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

