package opentutorials.season01.orand;

// row connect
public class OrDemo {
	public static void main(String[] args){	
		if(true || true){
			System.out.println("A");
		}
		if(true || false){
			System.out.println("B");
		}
		if(false || true){
			System.out.println("C");
		}
		if(false || false){
			System.out.println("D");
		}
	}

}
