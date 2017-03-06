package opentutorials.orientation.ex;

class Calculator02{
	public static int left;
	public static int right;
	public static void sum(){
		System.out.println("PLUS : "+(Calculator02.left+Calculator02.right));
	}
}
class Employee02{
	public static int period;
	public static int right;
	public static void sum(){
		System.out.println("SALARY : "+Employee02.right*Employee02.period);
	}
}

public class A2ClassExample02{
	public static void main(String[] args) {
		Calculator02.left = 10;
		Calculator02.right = 20;
		Calculator02.sum();
		
		Employee02.period = 3;
		Employee02.right = 500;
		Employee02.sum();
	}
}