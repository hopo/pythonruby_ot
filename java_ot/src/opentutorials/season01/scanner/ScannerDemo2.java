package opentutorials.season01.scanner;

import java.util.Scanner;

public class ScannerDemo2{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNextInt()){
			System.out.println(sc.nextInt()*1000);
		}
		System.out.println("close.");
		sc.close();
	}
}