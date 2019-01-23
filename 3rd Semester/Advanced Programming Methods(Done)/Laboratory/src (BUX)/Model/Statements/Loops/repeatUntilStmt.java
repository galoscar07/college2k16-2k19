package Model.Statements.Loops;

import Model.Expressions.Exp;
import Model.Expressions.notExp;
import Model.PrgState;
import Model.Statements.CompStmt;
import Model.Statements.IStmt;

public class repeatUntilStmt implements IStmt {
    IStmt localStmt;
    Exp localExp;

    public repeatUntilStmt(IStmt st, Exp ex){
        this.localExp = ex;
        this.localStmt = st;
    }


    @Override
    public PrgState execute(PrgState state)
    {
        IStmt stmt = new CompStmt(localStmt, new While(new notExp(localExp), localStmt));
        state.getStk().push(stmt);
        return null;
    }

    public String toString(){
        String rez = "";

        rez = rez + "repeat(" + this.localStmt.toString() + ")...until(" + this.localExp.toString()+")";

        return rez;
    }
}

