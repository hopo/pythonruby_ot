package opentutorials.season03.exception;

// checked exception.
class DivideException2 extends Exception{
	DivideException2(){
		super();
	}
	DivideException2(String message){
		super(message);
	}
}

class Calculator2{
	int left, right;
	public void setOprands(int left, int right){
		this.left = left;
		this.right = right;
	}
	public void divide(){
		if(right == 0){
			try {
				throw new DivideException("/? Could not divide by 0.");
			} catch (DivideException e) {
				e.printStackTrace();
			}
		}
	System.out.println((this.left/this.right)+"\n\n<Divide end>");
	}
}
public class CalculatorDemo2{
	public static void main(String[] args){
		Calculator2 c2 = new Calculator2();
		c2.setOprands(10,0);
		try{
			c2.divide();
		}catch(Exception e){
			System.out.println(e.getMessage()); 
		}
	}
}