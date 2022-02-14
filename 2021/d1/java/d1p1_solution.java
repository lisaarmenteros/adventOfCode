import java.io.*;
import java.util.*;
import java.io.File;

public class d1p1_solution {
    public static void main(String[] args) {
        File source = new File("../input/d1_input.txt");

        Scanner reader = null;
        try {
            reader = new Scanner(source);
            int increased = 0;
            int prevValue = 0;

            while (reader.hasNextLine()) {
                int line = Integer.parseInt(reader.nextLine());

                if (prevValue != 0 && line > prevValue) {
                    increased++;
                }

                prevValue = line;
            }

            System.out.print(increased);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}