package domain.statements.HeapStatements;

import domain.exp.Exp;
import domain.PrgState;
import domain.statements.IStmt;
import exception.*;

import java.io.IOException;

public class NewStmt implements IStmt {
    private String var;
    private Exp exp;
    public NewStmt(String var, Exp exp) {
        this.var = var;
        this.exp = exp;
    }
    @Override
    public PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException, UnknownComparisonExpression {
        int res = this.exp.eval(state.getSymTable(), state.getHeap());
        int loc = state.getHeap().allocate(res);
        state.getSymTable().put(var, loc);
        return null;
    }

    @Override
    public String toString() {
        return "newStmt(" + this.var + ", " + this.exp.toString() + ")";
    }
}
