import java.util.Scanner;

public class MCQchallenge {
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        String question = "What (System.out.println('abbcda'); will print?";
        String choice1 = "1. abbcds";
        String choice2 = "2. abfdsd";
        String choice3 = "3. abbcda";

        String correctans = choice3;
        System.out.println(question);
        System.out.println(choice1);
        System.out.println(choice2);
        System.out.println(choice3);
        System.out.println("\n");


        String input = null;
        while (input != correctans) {
            input = s.nextLine();
            if (input.equals(correctans)) {
                System.out.println("Awesome! Your Answer is correct.");
            } else {
                System.out.println("Wrong Answer..");
                System.out.println("Try Again..");
            }

        }


    }
}
