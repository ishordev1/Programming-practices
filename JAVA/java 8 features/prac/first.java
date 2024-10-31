package prac;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;
class A{
public	static void  printNameNTimes(int n){
	        if(n==0){
	            return;
	        }
	        System.out.println("Jhon");
	        
	        printNameNTimes(--n);
	    }

//print  1 to n
static void print1toN(int i,int n) {
	if(i>=n) {
		return;
	}
System.out.println(i);

print1toN(1+i,n);
}
}
public class first {
public static void main(String[] args) {
//	List<Integer> list=new ArrayList<>();
//	for(int i=1;i<100;i++) {
//		list.add(i);
//	}
//	list.stream().filter(n->n>50).forEach(f->System.out.println(f));

//Predicate<Integer> predcate=str->str.equals(100);
//System.out.println(predcate.test(898));
	
	A.print1toN(1,6);
	
	
}
}
