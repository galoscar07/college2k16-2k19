package Exceptions;

public class MyViewException extends Exception
{
    public MyViewException(MyControllerException msg) {super(msg);}
    public MyViewException(String msg) {super(msg);}
}
