package Model.Utils;
import Exceptions.MyStackException;
import Model.Expressions.Exp;
import Model.Statements.IStmt;

import java.util.Stack;

public interface MyIStack<T>{
    void push(T el);
    T pop();
    void isEmpty() throws MyStackException;
    Stack<T> getStk();
    void check(Exp exp, IStmt Stmt);
}

