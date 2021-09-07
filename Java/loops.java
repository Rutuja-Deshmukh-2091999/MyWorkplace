import java.util.Scanner;

public class loops {
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        boolean isonrepeat = true;
        while(isonrepeat){
            System.out.println("Playing your song on repeat");
            System.out.println("Do you want to exit ?");

            String a = s.nextLine();
            if (a.equals("yes"))
            {
                isonrepeat = false;
            }


        }
        System.out.println("Enjoy your next song");

    }
}
