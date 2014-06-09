public class Stack {
	private Node top = null;

	public void push(int data) {
		Node n = new Node(data);

		if (top == null) {
			top = n;
		} else {
			n.next = top;
			top = n;
		}
	}

	public Node pop() {
	    Node n = top;

		if (top != null) {
			top = top.next;
		}

		return n;
	}

	public int peek() {
		return top.data;
	}

	public String toString() {
		StringBuilder sb = new StringBuilder();

		Node current = top;

		while (current != null) {
			sb.append(current.data + " ");
			current = current.next;
		}

		return sb.toString();
	}

	public static void main(String[] args) {
        Stack s = new Stack();
        s.push(1);
        s.push(2);
        s.push(3);
        s.pop();
        s.push(5);
        System.out.println(s);
	}
}

class Node {
	int data;
	Node next;

	Node(int data) {
		this.data = data;
	}
}

