package Method_And_Constructor_Reference;
interface C{
	public void cons();
}
class student{
student() {
System.out.println("This is constructor");
}
void fun() {
	System.out.println("This is function");
}
}

public class constructor_Reference {
public static void main(String[] args) {

	C obj=student::new;
	
}
}
