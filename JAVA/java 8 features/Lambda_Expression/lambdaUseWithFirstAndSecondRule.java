package Lambda_Expression;
interface sum{
	int add(int a, int b);
}

interface stringLength{
	int stLength(String st);
}
public class lambdaUseWithFirstAndSecondRule {
public static void main(String[] args) {
//	first rule when interface has single statement then not need to keep curly bracket
	//second rule not need to use data type in the function parameter and
//	also not use return keyword when the function is return type
	
	
	//Applying first and second rule in this lambda function
	sum obj=(a,b)->a+b;
//System.out.println(obj.add(5, 7));
	
//	string length return
	stringLength obj2=(st)->st.length();
	System.out.println(obj2.stLength("my name is Jonn"));
}
}
