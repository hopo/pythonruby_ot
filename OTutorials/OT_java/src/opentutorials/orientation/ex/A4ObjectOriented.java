package opentutorials.orientation.ex;

public class A4ObjectOriented {
	public static void sum(int left, int right){
		System.out.println(left+right);
	}

	public static void main(String[] args) {
		int left =10;
		int right = 20;
		A4ObjectOriented.sum(left,right);
			
		left = 100;
		right = 200;
		A4ObjectOriented.sum(left,right);
	}
}