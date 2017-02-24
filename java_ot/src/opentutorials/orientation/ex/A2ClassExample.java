package opentutorials.orientation.ex;

class Calculator {	
	static int left;
	static int right;
	public static void sum(){
		System.out.println("PLUS : "+(Calculator.left+Calculator.right));
	}
}
	
class Employee {
	public static int period;
	public static int right;
	public static void sum(){
		System.out.println("SALARY : "+Employee.right*Employee.period);
	}
}
	
public class A2ClassExample {
	public static void main(String[] args) {
		Calculator.left = 10;
		Calculator.right = 20;
		Calculator.sum();
			
		Employee.period = 3;
		Employee.right = 500;
		Employee.sum();
	}
}