package opentutorials.season02.overloading;

public class OverloadingDemo3{
	void A(){System.out.println("void A()");}
	void A(int arg1){System.out.println("void A(int arg1)");}
	void A(String arg1){System.out.println("void A(String arg1)");}
	//int A(){System.out.println("int A()");}

	public static void main(String[] args){
		OverloadingDemo3 od=new OverloadingDemo3();
		od.A();
		od.A(1);
		od.A("a");
	}
}