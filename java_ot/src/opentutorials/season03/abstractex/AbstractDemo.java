package opentutorials.season03.abstractex;

abstract class A{
	public abstract int b();
	// Abstract member doesn't have body{}. ex) b();
	// When class has abstract member, that class is "abstract class".
	//public abstract int c(){System.out.println("Hello");}
	public void d(){
		System.out.println("World");
	}
}

class B extends A{
	public int b(){
		return 1;
	}	
}

public class AbstractDemo{
	public static void main(String[] args){
		//B obj=new B();
	}
}