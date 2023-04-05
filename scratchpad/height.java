
import java.util.Scanner;

public class Ride1 {

	public static void main(String[] args) {
		
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter your name: ");
		String name=sc.nextLine();
		System.out.println("Enter your age: ");
		int age=sc.nextInt();
		System.out.println("Enter your height: ");
		int height=sc.nextInt();
		
		String ifPic="";
		
		if(height>120) {
			System.out.println("Hey " +name+ " you can ride & get the ticket");
			if(age>45 && age<55) {
				System.out.println("Do you need a photograph? Answer 'yes' or 'no'\n"); 
				 ifPic = sc.nextLine();
				if(ifPic == "yes") {
					System.out.println("which cost $3");
				}
				
			}
		}

	}

	}