package opentutorials.season01.ex;

public class SwitchDemo{
public static void main(String [] args){
	/*
	System.out.println("0.if(val==1)");
	int val =1;
	if(val == 1){System.out.println("one");
	}else if(val == 2){System.out.println("two");
	}else if(val == 3){System.out.println("three");
	}
	*/
	
	System.out.println("1.switch(1)");
	switch(1){
		case 1:
			System.out.println("one");
		case 2:
			System.out.println("two");
		case 3:
			System.out.println("three");
	}

	System.out.println("2.switch(2)");
	switch(2){
		case 1:
			System.out.println("one");
		case 2:
			System.out.println("two");
		case 3:
			System.out.println("three");
	}

	System.out.println("3.switch(1) and break");
	switch(1){
		case 1:
			System.out.println("one");
			break;
		case 2:
			System.out.println("two");
			break;
		case 3:
			System.out.println("three");
			break;
	}
}
}
