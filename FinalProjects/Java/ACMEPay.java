import java.util.*;
public class ACMEPay {
    public static void main(String[] args) throws Exception 
    {
        int retire = 1;
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter shift - 1 , 2 , or 3");
        int shift = input.nextInt();
      //ask for hours worked
        double hours;
        System.out.println("Please enter hours worked");
        hours = input.nextDouble();
      //ask for participation in retirement plan if the second or third shift are selected
        if (shift == 2 || shift == 3){
            System.out.println("Do you participate in the retirement plan? (Y/N)");
            if (input.next().equals("Y")||input.next().equals("N")){
                retire = 1;
            }
            else{
                retire = 0;
            }

        }

        double rate = payRate(shift);
        double gross = grossPay(rate, hours);
        
        System.out.println("Hours worked is " + hours);
        System.out.println("Hourly pay rate is " + rate);
        hoursBreakdown(rate, hours);
        retirementPay(shift, retire, gross);
    }
    
    public static double payRate(int shift)
    {
        double wage = 0;
        if (shift == 1){
            wage = 17.00;
        } 
        else if (shift == 2){
            wage = 18.50;
        }
        else if (shift == 3){
            wage = 22.00;
        }
        else{  
        }  

        return wage;
    }

    public static void hoursBreakdown(double rate, double hours)
    {
        if (hours < 40){
            System.out.println("Your regular pay is $" + (hours));
            System.out.println("Your overtime pay is $0");
        }
        double overtime = 0;
        if (hours > 40){
            System.out.println("Your regular pay is $"+ (hours * rate));
            overtime = hours - 40;
            hours = Math.abs(hours - overtime);
            overtime = overtime * (rate * 1.5);
            System.out.println("Your overtime pay is $" + overtime);
        }
        
    }

    public static double grossPay(double rate, double hours)
    {
        double pay;
        pay = rate * hours;
  
        return pay;
    }

    public static void retirementPay(int shift ,int choice, double gross)
    {
        double netPay = gross;
        double retire = netPay * .03;
        if (shift == 2 || shift == 3){
            if (choice == 1){
                netPay = gross - (.03 * gross);
            }
            else if (choice == 0){
                netPay = gross;
            }
        }

        System.out.println("Retirment Deduction is " + retire);
        System.out.println("Net Pay is ...................." + netPay);
    }
}
