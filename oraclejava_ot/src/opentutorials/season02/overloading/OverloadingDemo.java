package opentutorials.season02.overloading;

class Calculator{
	int first, second;
	int third=0;

	public void setOprands(int first, int second){
		this.first=first;
		this.second=second;
	}
	public void setOprands(int first, int second, int third){
		this.setOprands(first,second);
		this.third=third;
	}

	public void sum(){
		System.out.println("sum: "+(this.first+this.second+this.third));
	}
	public void sub(){
		System.out.println("sub: "+(this.first-this.second-this.third));
	}
}

public class OverloadingDemo{
	public static void main(String[] args){
		Calculator c1=new Calculator();
		c1.setOprands(10,20);
		c1.sum();
		c1.sub();

		Calculator c2=new Calculator();
		c2.setOprands(50,10,20);
		c2.sum();
		c2.sub();
	}
}