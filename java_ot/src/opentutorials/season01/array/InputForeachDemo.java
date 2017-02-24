package opentutorials.season01.array;

class InputForeachDemo{
	public static void main(String[] args){
		for(String e : args){
			System.out.println(e);
		}
		System.out.println("ArgsLength : "+args.length);
	}
}