package opentutorials.season01.array;

public class GetDemo{
	public static void main(String[] args){
		//String[] classGroup ={"Andrei","Betty","Chris","Darcy"};
		
		String[] classGroup = new String[4];
		classGroup[0] = "Andrei";
		classGroup[1] = "Betty";
		classGroup[2] = "Chris";
		classGroup[3] = "Darcy";
		
		System.out.println("LENGTH : "+classGroup.length);
		
		System.out.println(classGroup[0]);
		System.out.println(classGroup[1]);
		System.out.println(classGroup[2]);
		System.out.println(classGroup[3]);
					
	}
}