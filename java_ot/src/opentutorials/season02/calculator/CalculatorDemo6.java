package opentutorials.season02.calculator;

class Calculator6{
	public static void sum(int left, int right){
		System.out.println(left+right);
	}

	public static void avg(int left, int right){
		System.out.println((left+right)/2);
	}
}

public class CalculatorDemo6{
	public static void main(String[] args){
		Calculator6.sum(10,20);
		Calculator6.avg(10,20);

		Calculator6.sum(20,40);
		Calculator6.avg(20,40);
	}
}