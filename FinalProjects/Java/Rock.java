import java.util.Scanner;
public class Rock
{
  public static void main(String[] args)
  {
    String personPlay; 
    String computerPlay; //Computer's play -- "R", "P", or "S"
    int computerInt; //Randomly generated number for computer play
    Scanner scan = new Scanner(System.in);
    int wins = 0;
    int loses = 0;
    int ties = 0;

    for (int i = 0; i < 10; i ++){ 
      System.out.println("Enter your play");
      personPlay = scan.nextLine();
      personPlay = personPlay.toUpperCase();
      if (personPlay.length() > 1){
        while (!(personPlay.substring(0,2).equals("SC") || personPlay.substring(0,2).equals("S") || personPlay.substring(0,2).equals("RO") || personPlay.substring(0,2).equals("R") || personPlay.substring(0,2).equals("PA") || personPlay.substring(0,2).equals("P") )){
          System.out.println("Invalid play. Try again: ");
          personPlay = scan.nextLine();
          personPlay = personPlay.toUpperCase();
        }
      }
      personPlay = personPlay.substring(0,1);
      computerInt = (int)(Math.random() * 3);
      if (computerInt == 0){
        computerPlay = "R";
      }
      else if (computerInt == 1){
        computerPlay = "P";
      }
      else{
        computerPlay = "S";
      }
      System.out.println("Computer play is " + computerPlay);
        
        //... Fill in rest of code
        //Print computer's play
        //See who won. Use nested ifs instead of &&.
      if (personPlay.equals(computerPlay)){
        System.out.println("It's a tie!");
        ties ++;
      }
      else if (personPlay.equals("R")){

        if (computerPlay.equals("S")){
          System.out.println("Rock crushes scissors. You win!");
          wins ++;
        }
        else{
          System.out.println("Paper covers rock. You Lose :(");
          loses ++;
        }
      }
      else if (personPlay.equals("S")){
        if (computerPlay.equals("R")){
          System.out.println("Rock crushes scissors. You Lose :(");
          loses ++;
        }
        else{
          System.out.println("Scissors cut paper. You win!");
          wins ++;
        }
      }
      else{
        if (computerPlay.equals("S")){
          System.out.println("Scissors cut paper. You lose :(");
          loses ++;
        }
        else{
          System.out.println("Paper covers rock. You win!");
          wins ++;
        }
      }
    }
    System.out.println("You lost " + loses);
    System.out.println("You won " + wins);
    System.out.println("You tied " + ties);
  }
  
}
