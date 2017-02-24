package opentutorials.season02.overriding;

class Calculator2{
	int left, right;

	public void setOprands(int left, int right){
		this.left=left;
		this.right=right;
	}
	public int sum(){
		return (this.left+this.right);
	}
}

class SubCalculator2 extends Calculator2{
	public int sum(){
		return super.sum();
	}
	public void sub(){
		System.out.println(this.left-this.right);
	}
}

public class OverridingDemo2{
	public static void main(String[] args){
		SubCalculator2 s1=new SubCalculator2();
		s1.setOprands(10,20);
		s1.sub();
		System.out.println(s1.sum());
	}
}