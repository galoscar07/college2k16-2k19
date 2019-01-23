package Model.Expressions;
import Exceptions.DivisionByZeroException;
import Exceptions.MyStmtException;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;

public class ArithExp extends Exp{
    Exp e1;
    Exp e2;
    int op; //1 stands for +, 2 for -, etc

    public ArithExp(int op,Exp e1,Exp e2){
        this.e1=e1;
        this.e2=e2;
        this.op=op;
    }
    //override
    public int eval(MyIDictionary<String,Integer> tbl, MyIHeap<Integer> hp)throws MyStmtException, DivisionByZeroException {
        try
        {
            if (op == 1)
                return e1.eval(tbl,hp) + e2.eval(tbl,hp);
            if (op == 2)
                return e1.eval(tbl,hp) - e2.eval(tbl,hp);
            if (op == 3)
                return e1.eval(tbl,hp) * e2.eval(tbl,hp);
            if (op == 4)
            {
                if (e2.eval(tbl,hp) == 0)
                    throw new DivisionByZeroException("Division by zero!!!");
                else
                    return e1.eval(tbl,hp) / e2.eval(tbl,hp);
            }
            else
                throw new MyStmtException("The operand does not exist!!");
        }
        catch (MyStmtException e)
        {
            throw new MyStmtException(e);
        }
    }


    public String toString() {
        if (op==1) return "("+e1+"+"+e2+")";
        if (op==2) return "("+e1+"-"+e2+")";
        if (op==3) return "("+e1+"*"+e2+")";
        if (op==4) return "("+e1+"/"+e2+")";
        return null;

    }
}
