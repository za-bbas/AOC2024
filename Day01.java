import java.util.*;
import java.io.*;
public class Day1 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("input1.txt");
        partOne(new Scanner(file));
        partTwo(new Scanner(file));
    }   
    public static void partOne(Scanner file){
        int distance = 0;
        List<Integer> right = new ArrayList<>();
        List<Integer> left = new ArrayList<>();
        while(file.hasNextLine()){
            String[] line = file.nextLine().split(" ");
            left.add(Integer.parseInt(line[0]));
            right.add(Integer.parseInt(line[line.length-1]));
        }
        Collections.sort(left);
        Collections.sort(right);
        for(int i = 0; i<left.size(); i++){
            distance += Math.abs(left.get(i) - right.get(i));
        }
        System.out.println(distance);
    }
    public static void partTwo(Scanner file){
        int similarity = 0;
        List<Integer> right = new ArrayList<>();
        List<Integer> left = new ArrayList<>();
        while(file.hasNextLine()){
            String[] line = file.nextLine().split(" ");
            left.add(Integer.parseInt(line[0]));
            right.add(Integer.parseInt(line[line.length-1]));
        }
        Map<Integer, Integer> frequency = new HashMap<>();
        for(int n: right){
            if(frequency.containsKey(n)){
                frequency.put(n, frequency.get(n)+1);
            }else{
                frequency.put(n, 1);
            }
        }
        for(int n : left){
            similarity += frequency.getOrDefault(n, 0)*n;
        }
        System.out.println(similarity);
    }
}