package Exceptions;

public class MyStmtException extends Exception
{
    public MyStmtException(MyDictionaryException msg) {super(msg);}
    public MyStmtException(MyStmtException msg) { super(msg);}
    public MyStmtException(String s) { super(s);}
}
