package Exceptions;

public class MyControllerException extends Exception
{
    public MyControllerException(MyStmtException msg) {super(msg);}
    public MyControllerException (String msg) {super(msg);}
    public MyControllerException(MyControllerException e) { super(e);}
    public MyControllerException(DivisionByZeroException e) {super(e);}

    public MyControllerException(MyDictionaryException e) {
    }
}
