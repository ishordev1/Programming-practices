package Lambda_Expression;
interface A{
	void fun();
	void fun2();
}

public class anonymous_class {
	public static void main(String[] args) {
		FirstInterface obj= new FirstInterface(){
			public void fun() {
				System.out.println("hello");
			}
		};
		
		//calling anonymous class
//		obj.fun();
		
		
		
		
		A ob1=new A() {
		public	void fun() {
				
			}
		public	void fun2() {
				
			}
		};
		
	}
}
