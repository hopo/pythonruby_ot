package opentutorials.season02.calculator;

class Calculator7{
	int left, right;

	public Calculator7(int left, int right){
		this.left=left;
		this.right=right;
	}

	public void sum(){
		System.out.println(this.left+this.right);
	}
	public void avg(){
		System.out.println((this.left+this.right)/2);
	}
}

public class CalculatorDemo7{
	public static void main(String[] args){
		Calculator7 c1=new Calculator7(10,20);
		c1.sum();
		c1.avg();

		Calculator7 c2=new Calculator7(30,40);
		c2.sum();
		c2.avg();
	}
}