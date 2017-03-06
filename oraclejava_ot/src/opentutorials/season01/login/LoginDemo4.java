package opentutorials.season01.login;

public class LoginDemo4{
	public static void main(String [] args){
		String id = args[0];
		String pw = args[1];
		if((id.equals("hpsight") || id.equals("coon1101") || id.equals("hp1101"))
		&& pw.equals("3699")){
			System.out.println("welcome");
		}else{
			System.out.println("wrong");
		}
	}
}
