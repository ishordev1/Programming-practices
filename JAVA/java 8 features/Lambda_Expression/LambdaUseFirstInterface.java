package Lambda_Expression;


public class LambdaUseFirstInterface {
public static void main(String[] args) {
	
	FirstInterface obj=()->{
		System.out.println("First Lambda Rule apply with curly bracket");
	};

	FirstInterface obj2=()->
	System.out.println("Second Lambda Rule apply");
	
	obj2.fun();
	obj.fun();
}
}
