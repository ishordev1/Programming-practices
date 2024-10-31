package Stream_API;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class StringUpperCaseConvert {
    public static void main(String[] args) {
        String s = "my name is john";
        List<String> list = new ArrayList<>();

        // Split the string by spaces and add each word to the list
        for (String word : s.split(" ")) {
            list.add(word);
        }

        // Convert the first letter of each word to uppercase using Streams
        List<String> result = list.stream()
                                 .map(word -> word.substring(0, 1).toUpperCase() + word.substring(1))
                                 .collect(Collectors.toList());

        // Print the result
        result.forEach(System.out::println);
    }
}
