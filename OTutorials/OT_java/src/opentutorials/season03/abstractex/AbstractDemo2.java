package opentutorials.season03.abstractex;

abstract class Calculator{
	int left, right;
	int _sum(){
		return this.left+this.right;
	}
	public void setOprands(int left, int right){
		this.left=left;
		this.right=right;
	}
	public abstract void sum();
	public abstract void avg();
	public void run(){
		sum();
		avg();
	}
}

class CalculatorDecoPlus extends Calculator{
	public void sum(){
		System.out.println("+sum+ "+_sum());
	}
	public void avg(){
		System.out.println("+avg+ "+(_sum()/2));
	}
}

class CalculatorDecoMinus extends Calculator{
	public void sum(){
		System.out.println("-sum- "+_sum());
	}
	public void avg(){
		System.out.println("-avg- "+(_sum()/2));
	}
}

public class AbstractDemo2{
	public static void main(String[] args){
		CalculatorDecoPlus C1=new CalculatorDecoPlus();
		C1.setOprands(10,20);
		C1.run();

		CalculatorDecoMinus C2=new CalculatorDecoMinus();
		C2.setOprands(20,30);
		C2.run();	
	}
}