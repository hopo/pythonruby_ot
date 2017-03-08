package opentutorials.season02.overriding;

class Calculator{
	int left, right;

	public void setOprands(int left, int right){
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

class SubCalculator extends Calculator{
	public void sum(){
		System.out.println("Answer is "+(this.left+this.right));
	}
	public void sub(){
		System.out.println(this.left-this.right);
	}
}

public class OverridingDemo{
	public static void main(String[] args){
		SubCalculator s1=new SubCalculator();
		s1.setOprands(10,20);
		s1.sum();
		s1.avg();
		s1.sub();
	}
}