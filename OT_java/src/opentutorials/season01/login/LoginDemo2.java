package opentutorials.season01.login;

public class LoginDemo2 {
	public static void main (String [] args){
		String id = args[0];
		String pw = args[1];
		if (id.equals("hpsight")){
			if(pw.equals("3699")){
				System.out.println("welcome");
			}else{
				System.out.println("wrong pw");
			}
		}else{
			System.out.println("wrong id");
		}
	}
}
