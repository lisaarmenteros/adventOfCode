import java.io.*;
import java.util.*;

public class d1p2_solution {

    public static List<Integer> getFileInput() {
        File inputFile = new File("../input/d1_input.txt");
        List<Integer> submarineDepths = new ArrayList<Integer>();

        try {
            Scanner inputScanner = new Scanner(inputFile);

            while (inputScanner.hasNextLine()) {
                submarineDepths.add(Integer.parseInt(inputScanner.nextLine()));
            }
            inputScanner.close();
        } catch (IOException e) {
            System.out.println(e);
        }

        return submarineDepths;
    }

    public static int depthSweep(List<Integer> submarineDepths) {
        int count = 0;

        for (int i = 0; i < submarineDepths.size() - 3; i++) {
            if ((submarineDepths.get(i + 1) + submarineDepths.get(i + 2)
                    + submarineDepths.get(i + 3)) > (submarineDepths.get(i) + submarineDepths.get(i + 1)
                            + submarineDepths.get(i + 2)))
                count++;
        }

        return count;
    }

    public static void main(String[] args) {
        List<Integer> submarineDepths = getFileInput();

        System.out.println(depthSweep(submarineDepths));
    }
}
