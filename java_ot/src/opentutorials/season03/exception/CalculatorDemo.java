package opentutorials.season03.exception;

// unchecked exception.
class DivideException extends RuntimeException{
	public int left, right;
	DivideException(){
		super();
	}
	DivideException(String message){
		super(message);
	}
	DivideException(String message,int left,int right){
		super(message);
		this.left = left;
		this.right = right;
	}
}

class Calculator{
	int left, right;
	public void setOprands(int left, int right){
		this.left = left;
		this.right = right;
	}
	public void divide(){
		if(right == 0){
			throw new DivideException("/? Could not divide by 0.",this.left,this.right);
		}
	System.out.println((this.left/this.right)+"\n\n<Divide end>");
	}
}
public class CalculatorDemo{
	public static void main(String[] args){
		Calculator c1 = new Calculator();
		c1.setOprands(10,0);
		try{
			c1.divide();
		}catch(DivideException e){
			System.out.println(e.getMessage());
			System.out.println(e.left);
			System.out.println(e.right);
		}
	}
}