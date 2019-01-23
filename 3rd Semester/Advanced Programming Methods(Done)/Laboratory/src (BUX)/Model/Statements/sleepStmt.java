package Model.Statements;

import Exceptions.MyStmtException;
import Model.Expressions.ConstExp;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;
import Model.Utils.MyIStack;

public class sleepStmt implements IStmt{
    Exp number;

    public sleepStmt(Exp nr){
        this.number = nr;
    }

    public PrgState execute(PrgState state){
        MyIStack<IStmt> localStack= state.getStk();
        MyIDictionary<String, Integer> localSym = state.getSymTable();
        MyIHeap<Integer> localHeap = state.getHeap();

        Integer nr = null;
        try {
            nr = this.number.eval(localSym,localHeap);
        } catch (MyStmtException e) {
            e.printStackTrace();
        }
        Integer nr1 = nr;

        if(nr > 0){
            nr1  = nr - 1;
            localStack.push(new sleepStmt(new ConstExp(nr1)));
        }
        return null;
    }

    public String toString(){
        String rez = "";
        rez = rez + "sleep(" + this.number.toString() + ")";
        return rez;
    }
}

