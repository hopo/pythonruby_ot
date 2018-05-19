package opentutorials.season02.overloading;

class Calculator2{
	int first, second;

	public Calculator2(int first, int second){
		this.first=first;
		this.second=second;
	}
	
	public void sum(){
		System.out.println("sum: "+(this.first+this.second));
	}
}

class thirdCalculator extends Calculator2{
	int third;

	public thirdCalculator(int first, int second, int third){
		super(first,second);
		this.third=third;
	}

	public void sum(){
		System.out.println("3sum: "+(this.first+this.second+this.third));
	}
}

public class OverloadingDemo2{
	public static void main(String[] args){
		Calculator2 c1=new Calculator2(10,20);
		c1.sum();

		thirdCalculator c2=new thirdCalculator(100,10,20);
		c2.sum();
	}
}