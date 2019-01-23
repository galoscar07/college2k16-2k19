package Exceptions;

public class MyStmtExecException extends Exception
{
    public MyStmtExecException(MyStackException msg) {super(msg);}
}
