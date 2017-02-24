package opentutorials.season03.exception;

import java.io.IOException;

class E{
	void throwArithmericException(){
		throw new ArithmeticException();
	}
	void throwIOException1(){
		try {
			throw new IOException();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	void throwIOException2() throws IOException{
		throw new IOException();
	}
}