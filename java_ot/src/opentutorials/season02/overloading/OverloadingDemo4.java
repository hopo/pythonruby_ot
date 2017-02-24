package opentutorials.season02.overloading;

public class OverloadingDemo4 extends OverloadingDemo3{
	void A(String arg1, String arg2){
		System.out.println("sub class: void A(String arg1, String arg2)");
	}
	void A(){
		System.out.println("sub class: void A()");
	}
	public static void main(String[] args){
		OverloadingDemo4 od=new OverloadingDemo4();
		od.A();
		od.A(1);
		od.A("a");
		od.A("a","b");
	}
}