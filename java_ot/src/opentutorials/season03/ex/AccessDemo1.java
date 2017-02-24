package opentutorials.season03.ex;

class A{
	public String y(){
		return "public void y()";
	}
	private String z(){
		return "public void z()";
	}
	public String x(){
		return z();
	}
}

public class AccessDemo1{
	public static void main(String[] args){
		A a=new A();
		System.out.println(a.y());
		// error code that below
		//System.out.println(a.z());
		System.out.println(a.x());
	}
}