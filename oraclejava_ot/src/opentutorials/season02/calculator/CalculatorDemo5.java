package opentutorials.season02.calculator;

class Calculator5 {
	static double PI=3.14;
	static int base=0;
	int left,right;

	public void setOprands(int left, int right){
		this.left=left;
		this.right=right;
	}

	public void sum(){
		System.out.println(this.left+this.right+(short)(base*PI));
	}
	public void avg(){
		System.out.println((this.left+this.right)/2);
	}
}

public class CalculatorDemo5{
	public static void main(String[] args){
		Calculator5 c5a=new Calculator5();
		c5a.setOprands(10,20);
		c5a.sum();
		c5a.avg();

		Calculator5 c5b=new Calculator5();
		c5b.setOprands(30,40);
		c5b.sum();
		c5b.avg();
		
		Calculator5.base=100;
		c5a.sum();
		c5b.sum();
	}
}