package Model.Expressions;

import Exceptions.MyStmtException;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;

public class Boolean extends Exp{
    private Exp e1;
    private Exp e2;
    private String op;

    public Boolean(Exp exp1, Exp exp2,String operator){
        this.e1=exp1;
        this.e2=exp2;
        this.op=operator;
    }

    public int eval(MyIDictionary<String, Integer> tbl, MyIHeap<Integer> hp) throws MyStmtException {
        try {
            if (op == "<")
                if (e1.eval(tbl, hp) < e2.eval(tbl, hp))
                    return 1;
                else
                    return 0;
            if (op == "<=")
                if (e1.eval(tbl, hp) <= e2.eval(tbl, hp))
                    return 1;
                else
                    return 0;
            if (op == ">")
                if (e1.eval(tbl, hp) > e2.eval(tbl, hp))
                    return 1;
                else
                    return 0;

            if (op == ">=")
                if (e1.eval(tbl, hp) >= e2.eval(tbl, hp))
                    return 1;
                else
                    return 0;

            if (op == "==")
                if (e1.eval(tbl, hp) == e2.eval(tbl, hp))
                    return 1;
                else
                    return 0;
            if (op == "!=")
                if (e1.eval(tbl, hp) != e2.eval(tbl, hp))
                    return 1;
                else
                    return 0;
            else throw new MyStmtException("The operand does not exist!!!");
        }
        catch(MyStmtException e){
            throw new MyStmtException(e);
        }

    }

    public String toString() {
        return "("+e1.toString()+op+e2.toString()+")";
    }
}
