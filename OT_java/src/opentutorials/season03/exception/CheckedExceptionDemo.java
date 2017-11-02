package opentutorials.season03.exception;

import java.io.*;
public class CheckedExceptionDemo{
	public static void main(String[] args){
		BufferedReader bReader = null;
		try {
			bReader = new BufferedReader (new FileReader("srcbin/out.txt"));
		} catch (FileNotFoundException e) {
			System.out.println("FileNotFoundException e");
			e.printStackTrace();
		}
		String input = null;
		try {
			input = bReader.readLine();
		} catch (IOException e) {
			System.out.println("IOException e");
			e.printStackTrace();
		}
		System.out.println(input);
	}
}