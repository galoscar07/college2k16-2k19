package Model.Expressions;
import Exceptions.MyStmtException;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;

import java.lang.Integer;
import java.lang.String;

public abstract class Exp {
    public abstract int eval(MyIDictionary<String,Integer> tbl, MyIHeap<Integer> hp) throws MyStmtException;
    public abstract String toString();//again you may want to use toString instead of this toStr
}
