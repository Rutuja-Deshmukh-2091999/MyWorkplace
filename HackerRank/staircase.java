import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class staircase {

    /*
     * Complete the 'staircase' function below.
     *
     * The function accepts INTEGER n as parameter.
     */

    public static void staircase(int n) {
        // Write your code here
        int i, j, num = 1, k;

        for (i = 1; i <= n; i++) //outer loop for number of rows(n)
        {

            for (j = n - 1; j >= i; j--) //  inner loop for columns
            {
                System.out.print(" ");

            }
            for (k = 1; k <= i; k++) {
                System.out.print("*");
            }
            System.out.println(); // ending line after each row
        }


    }


    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        staircase(n);

        bufferedReader.close();
    }
}