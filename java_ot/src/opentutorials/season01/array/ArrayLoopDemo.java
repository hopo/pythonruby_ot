package opentutorials.season01.array;

public class ArrayLoopDemo{

	public static void main (String[] args){
		String[] members = {"Andrei", "Betty", "Chris"};
		
		/*
		for(int i=0; i<members.length; i++){
			String member = members[i];
			System.out.println(member+" is called.");
		}
		*/
		for(String e : members){
			System.out.println(e+" is called.");
			
		}
	}
}
