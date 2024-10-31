package Lambda_Expression;
interface D{
void show();
}

interface B{
	void show();
	void sum();
}

interface sum1{
	void fun(int a, int b);
}


public class test_lambda {
public static void main(String[] args) {
	D obj=new D() {
public	void show() {
	System.out.println("hello");	
	}
public void sum() {
	System.out.println("this is sum");
}
	};
	obj.show();
	
	
	D obj2=()->System.out.println("this is lambda");	
	obj2.show();
	
	
	sum1 obj3=(a,b)->System.out.println(a+b);
	obj3.fun(9, 9);
	
	
	
	Runnable th=()->
	{
	for(int i=1;i<99;i++) {
		System.out.println("thread");
	}
	};
	
	Thread t1=new Thread(th);
	t1.start();
}


}
