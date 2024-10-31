package Stream_API;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class filter_even_num {
public static void main(String[] args) {
//	without Stream API
	
//	List<Integer> list= List.of(4,5,6,3,6);
//	List<Integer> evenList=new ArrayList<>();
//for(Integer i:list) {
//	if(i%2==0) {
//		evenList.add(i);
//	}
//}
//	System.out.println(evenList);
	
	
	
	List<Integer> list=List.of(2,3,4,5,6,7,8,9,10);
	Stream<Integer> stream=list.stream();
	List<Integer> newList=stream.filter(i->i%2==0).collect(Collectors.toList());
	
	String []name= { "Ishor", "Dinest", "Nabin"};
	for(String n:name) {
		System.out.println(n.charAt(0));
	}
}
}
