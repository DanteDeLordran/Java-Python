import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class JavaMaster {
    public static void main(String[] args) {
        System.out.println("Te amo Blanca");

        //Array
        int[] numbersArray = new int[4];
        numbersArray[0] = 1;
        
        //List
        List<Integer> numbersList = new ArrayList<>();
        numbersList.add(1);
        numbersList.remove(numbersList.indexOf(1));
        int size = numbersList.size();
        List<Integer> anotherList = new ArrayList<>();
        numbersList.addAll(anotherList);
        numbersList.clear();

        //Set
        Set<Integer> someSet = new HashSet<>();
        someSet.add(1);
        someSet.add(2);
        someSet.add(2);
        boolean belongs = someSet.contains(7);
        
        //Map
        Map<String, int[]> studentScores = new HashMap<>();
        studentScores.put("dante", new int[]{100, 100, 100});
        studentScores.put("blanca", new int[]{100, 100, 100});

        //Ternary operator
        String message = true ? "Te amo blanca" : "Como quiera te amo";

        //For each 
        String[] nameList = {"Dante", "Blanca"};
        for (String name : nameList) {
            System.out.println(name);
        }

        //For (Python for in range)
        for (int i = 0; i < 5; i++) {
            System.out.println("Tas bien chula bb");
        }

        //(For enum in Python)
        String[] anotherNameList = {"Dante", "Blanca"};
        for (int i = 0; i < anotherNameList.length; i++) {
            System.out.println(anotherNameList[i]);
        }
    }
}
