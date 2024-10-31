package Lambda_Expression;


public class create_Thread_with_lambda{
public static void main(String[] args) {

Runnable thread=()->{
	for(int i=1;i<100;i++) {
		System.out.println(i);
		try {
			Thread.sleep(1000);
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
};


Thread t1=new Thread(thread);
t1.start();
}
}
