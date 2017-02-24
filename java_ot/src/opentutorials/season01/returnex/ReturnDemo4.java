package opentutorials.season01.returnex;

public class ReturnDemo4{
	public static String[] getMembers(){
		String[] members = {"Andrei", "Betty", "Chris"};
		return members;
	}

	public static void main(String[] args){
		String[] members = getMembers();
		System.out.println(members[1]);
	}
}
