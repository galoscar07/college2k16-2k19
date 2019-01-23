package Model.Utils;
import Exceptions.MyStackException;
import Model.Expressions.Exp;
import Model.Statements.IStmt;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;


public class MyStack<T> implements MyIStack<T> {

    private Stack<T> stk;
    public MyStack()
    {
        stk=new Stack<T>();
    }


    public void push(T el){
        stk.push(el);
    }

    public String toString(){
        List<T> stack= new ArrayList<>(stk);
        Collections.reverse(stack);
        String msg= "";
        for(T el:stack){
            msg+=el+";";
        }return msg;
    }
    public T pop(){
        return stk.pop();
    }
    public void isEmpty() throws MyStackException{
        if (stk.isEmpty())
            throw new MyStackException("Empty stack!");
    }
    public Stack<T> getStk(){
        return stk;
    }
    public void check(Exp exp, IStmt stmt){
        if (stk.pop()==exp)
            stk.push((T) stmt);

    }
}
