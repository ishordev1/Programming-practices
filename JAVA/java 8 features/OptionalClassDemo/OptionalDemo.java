package OptionalClassDemo;
//this class is used to handle null pointer Exception.
//It has 3 method to make optional class.  empty, of, ofNullable

import java.util.Optional;

public class OptionalDemo {
	public static Optional<String> getName(){
		String name=null;
		return Optional.ofNullable(name);
	}
public static void main(String[] args) {
	String st=null;
	Optional<String> op=Optional.ofNullable(st);
	System.out.println(op.isPresent());
//	System.out.println(op.get());
	System.out.println(op.orElse("it has no objet."));
	System.out.println(op.empty());
	
	
	
	Optional<String> opName = getName();
	System.out.println(opName.orElse("user not fooound"));
	
}
}
