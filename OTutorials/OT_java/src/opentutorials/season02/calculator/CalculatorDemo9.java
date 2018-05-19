package opentutorials.season02.calculator;

class MultiplicationableCalculator extends SubstractionableCalculator{
	public void multi(){
		System.out.println(this.left*this.right);
	}
}

public class CalculatorDemo9{
	public static void main(String[] args){
		MultiplicationableCalculator m1=new MultiplicationableCalculator();
		m1.setOprands(10,20);
		m1.sum();
		m1.avg();
		m1.sub();
		m1.multi();
	}
}