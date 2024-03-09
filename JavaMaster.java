import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.function.BinaryOperator;
import java.util.stream.Collectors;

public class JavaMaster {
    public static void main(String[] args) {
        System.out.println("Te amo Blanca");

        // Array
        int[] numbersArray = new int[4];
        numbersArray[0] = 1;

        // List
        List<Integer> numbersList = new ArrayList<>();
        numbersList.add(1);
        numbersList.remove(numbersList.indexOf(1));
        int size = numbersList.size();
        List<Integer> anotherList = new ArrayList<>();
        numbersList.addAll(anotherList);
        numbersList.clear();

        // Set
        Set<Integer> someSet = new HashSet<>();
        someSet.add(1);
        someSet.add(2);
        someSet.add(2);
        boolean belongs = someSet.contains(7);

        // Map
        Map<String, int[]> studentScores = new HashMap<>();
        studentScores.put("dante", new int[] { 100, 100, 100 });
        studentScores.put("blanca", new int[] { 100, 100, 100 });

        // Ternary operator
        String message = true ? "Te amo blanca" : "Como quiera te amo";

        // For each
        String[] nameList = { "Dante", "Blanca" };
        for (String name : nameList) {
            System.out.println(name);
        }

        // For (Python for in range)
        for (int i = 0; i < 5; i++) {
            System.out.println("Tas bien chula bb");
        }

        // (For enum in Python)
        String[] anotherNameList = { "Dante", "Blanca" };
        for (int i = 0; i < anotherNameList.length; i++) {
            System.out.println(anotherNameList[i]);
        }
    }

    private void someFunc() {
        System.out.println("Do something");
    }

    // Higher order function MAP
    List<String> nameList = Arrays.asList("Dante", "Blanca");
    List<String> nameListUppercase = nameList.stream()
            .map(String::toUpperCase)
            .collect(Collectors.toList());

    // Higher order function FILTER
    List<Integer> anotherNumberList = Arrays.asList(1, 2, 3, 3, 4, 7, 0, 5, 5);
    List<Integer> isOdd = anotherNumberList.stream()
            .filter(n -> n % 2 == 0)
            .collect(Collectors.toList());

    List<Student> students = Arrays.asList(
            new Student("Dante", 22, 100),
            new Student("Blanca", 21, 100));


    // Higher order function SORT
    List<Student> sortedListStudents = students.stream()
            .sorted((s1, s2) -> Integer.compare(s1.getAge(), s2.getAge()))
            .collect(Collectors.toList());

    // Higher order function REDUCE
    List<Integer> numbers = Arrays.asList(6, 6, 6, 6, 6, 6, 6, 6);
        BinaryOperator<Integer> op = (x, y) -> (x + y) * 2;
        int total = numbers.stream().reduce(0, op);

}

// Classes
public class User {

    private String name;

    private String password;

    public User(String name, String password) {
        this.name = name;
        this.password = password;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String saySomething(){
        return "I hate communists";
    }
}

// Inheritance
public class Student extends User {

    private String registration;

    public Student(String name, String password, String registration) {
        super(name, password);
        this.registration = registration;
    }

    public String getRegistration() {
        return registration;
    }

    public void setRegistration(String registration) {
        this.registration = registration;
    }

}