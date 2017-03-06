package opentutorials.season01.login;

public class LoginDemo{
	public static void main(String[] args){
		String id = args[0];
		
		if(id.equals("hpsight")){
			System.out.println("right");
		}else{
			System.out.println("wrong");
		}
	}
}