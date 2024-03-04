import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
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
        int listSize = numbersList.size();

        //Set
        Set<Integer> numbersSet = new HashSet<>();
        numbersSet.add(1);
        numbersSet.remove(1);

        

    }
}
