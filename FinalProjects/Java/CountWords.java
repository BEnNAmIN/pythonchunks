import java.util.Scanner;
public class CountWords
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a string: ");
        
        String sentence = input.nextLine();
        sentence += " ";
        
        int word_count = 0;
        boolean last = false;
        

        for (int i = 0; i < sentence.length(); i ++){
            String letter = sentence.substring(i, i + 1);
            if (letter.equals("?") || letter.equals(" ") || letter.equals(".") || letter.equals(";") || letter.equals("!") || letter.equals("-")){
                last = false;
            }
            else if (last == false){
                last = true;
                word_count ++;
            }
                
            
        }
        System.out.println("There are " + word_count + " words in the string");   
    }
}