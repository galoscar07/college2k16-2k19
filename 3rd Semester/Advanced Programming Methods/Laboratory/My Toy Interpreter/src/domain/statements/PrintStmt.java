package domain.statements;

import domain.exp.Exp;
import domain.adt.MyIList;
import domain.PrgState;
import exception.DivideByZeroException;
import exception.UnknownComparisonExpression;
import exception.UnknownVariableException;

public class PrintStmt implements IStmt {
    private Exp exp;

    public PrintStmt(Exp exp) {
        this.exp = exp;
    }

    @Override
    public String toString() {
        return "print(" + exp + ")";
    }

    @Override
    public PrgState execute(PrgState state) throws UnknownVariableException, DivideByZeroException, UnknownComparisonExpression {
        MyIList<Integer> out = state.getOut();
        out.add(exp.eval(state.getSymTable(), state.getHeap()));
        return null;
    }
}
