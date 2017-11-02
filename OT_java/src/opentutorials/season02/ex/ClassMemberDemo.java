package opentutorials.season02.ex;

class theC{
	static int sVariable=1;
	int nVariable=2;

	static void sMethod_sv(){
		System.out.println(sVariable);
	}
	static void sMethod_nv(){
		//System.out.println(iVariable);
	}

	void nMethod_sv(){
		System.out.println(sVariable);
	}
	void nMethod_nv(){
		System.out.println(nVariable);
	}
}

public class ClassMemberDemo{
	public static void main(String[] arg){
		//theC.sMethod_sv(); //1
		//theC.sMethod_nv(); //error
		//theC.nMethod_sv(); //error
		//theC.nMethod_nv(); //error
		
		theC iC=new theC();
		//iC.sMethod_sv(); //1
		//iC.sMethod_nv(); //error
		//iC.nMethod_sv(); //1
		//iC.nMethod_nv(); //2
	}
}