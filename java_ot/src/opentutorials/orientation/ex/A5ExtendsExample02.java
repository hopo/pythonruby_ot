package opentutorials.orientation.ex;

class CalcuZ {
	int Zleft, Zright;
	
	public void setting(int setleft, int setright){
		Zleft=setleft;
		Zright=setright;
	}
	
	public void sum(){
		System.out.println(Zleft+Zright);
	}
	public void avg(){
		System.out.println((Zleft+Zright)/2);
	}
}

class ExCalcuZ extends CalcuZ{
	public void multi(){
		System.out.println(Zleft*Zright);
	}
}

public class A5ExtendsExample02 {
	public static void main(String[] args){
		ExCalcuZ ecz = new ExCalcuZ();
		ecz.setting(10,20);
		ecz.sum();
		ecz.avg();
		ecz.multi();
	}
}