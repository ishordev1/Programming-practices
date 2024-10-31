package Method_And_Constructor_Reference;

interface A {
	void sum(int a, int b);
}

class B {
	static void add(int a, int b) {
		System.out.println((a + b));
	}

	static void fun() {
		System.out.println("this is method");
	}
}

//It work only when the interface has one method it is alternative of lambda expression
//parameter will be same in interface method and reference method
//return type don't matter
public class MethodReference {
	public static void main(String[] args) {
		// In lambda expression we make interface body with shortcut trick
		// but in Method reference we not need to make it body we refere other class method
		// which has same work in and same parameter in the method
		
		//refere other method body not need to make
		A obj = B::add;
		obj.sum(5, 6);

	}

}
