package Collection;

import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

public class HasMap {
public static void main(String[] args) {
	HashMap<String, String> has=new HashMap<>();
has.put("Book1","DSA" );
has.put("Book2", "Grammer");
has.put("Book3", "Science");
	has.put("Book4", "Angular");
//	 for (Map.Entry<String,String> map : has.entrySet()) {
//         String key = map.getKey();
//         String val=map.getValue();
//	System.out.print(key +" "+val +" ");
//}

	
	
	has.forEach((j,k)->{
		System.out.println(j+"-"+k);
	});
	
	
	
	
//
//	has.forEach((k,v)->{
//		System.out.print("["+k+" "+v+ "]");
//	});
//	System.out.println();
//	
//	
//	LinkedHashMap<String, String> lh=new LinkedHashMap<>();
//	lh.put("Book1","DSA" );
//	lh.put("Book4", "Angular");
//	lh.put("Book3", "Science");
//	lh.put("Book2", "Grammer");
//	System.out.println();
//lh.forEach((l,m)->{
//	System.out.print("["+l+" "+m+ "]");
//});
}
}
