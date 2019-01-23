package domain.statements.Loops;

import domain.PrgState;
import domain.exp.BoolExp;
import domain.exp.Exp;
import domain.exp.NotExp;
import domain.statements.CompStmt;
import domain.statements.IStmt;

public class RepeatUntilStmt implements IStmt{
    IStmt stmt;
    Exp exp;

    public RepeatUntilStmt(IStmt stmt, Exp exp){
        this.stmt = stmt;
        this.exp = exp;
    }

    @Override
    public PrgState execute (PrgState state){
        IStmt stmt = new CompStmt(this.stmt, new WhileStmt(this.exp, this.stmt));
        state.getExeStack().push(stmt);
        return null;
    }
    @Override
    public String toString(){
        String rez = "";
        rez = rez + "do(" + this.stmt.toString() + ")...while(" + this.exp.toString()+")";
        return rez;
    }
}
