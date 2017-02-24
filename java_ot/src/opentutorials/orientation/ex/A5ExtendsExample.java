package opentutorials.orientation.ex;

class CalcuA5 {
	public int left, right;
	
	public void sum(){
		System.out.println(left+right);
	}
	public void avg(){
		System.out.println((left+right)/2);
	}
}

class MultiCalcuA5 extends CalcuA5 {
	public void multi(){
		System.out.println(left*right);
	}
}

public class A5ExtendsExample {
	public static void main(String[] args){
		MultiCalcuA5 mc1 = new MultiCalcuA5();
		mc1.left = 10;
		mc1.right = 20;
		mc1.sum();
		mc1.avg();
		mc1.multi();
	}
}