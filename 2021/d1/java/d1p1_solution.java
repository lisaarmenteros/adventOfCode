import java.io.*;
import java.util.*;

public class d1p1_solution {
    public static void main(String[] args) {
        int count = 0;
        int prev = 0;

        try {
            File inputFile = new File("../input/d1_input.txt");
            Scanner inputFileScanner = new Scanner(inputFile);

            // Read while the file has a next line
            while (inputFileScanner.hasNextLine()) {
                int depth = Integer.parseInt(inputFileScanner.nextLine());

                if (prev != 0 && depth > prev)
                    count += 1;

                prev = depth;
            }

            System.out.println(count);

            inputFileScanner.close();
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}