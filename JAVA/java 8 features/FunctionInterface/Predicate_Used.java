package FunctionInterface;

import java.util.function.Predicate;
class A implements Predicate{

	@Override
	public boolean test(Object t) {
		
		if(t.equals(343)) {
			return false;
		}
		else {
			return true;
		}
	
	}
	
}
public class Predicate_Used {
public static void main(String[] args) {
	
	//Predicate Use with lambda expression
	Predicate<Integer> predicate=num->num.equals(189);
	System.out.println(predicate.test(89));
	
	Predicate<String> predicate1=num->num.equals("test");
	System.out.println(predicate1.test("test"));
	
	
	
	//predicate use with creating extra class
	A obj=new A();
	System.out.println(obj.test(3412));
}
}
