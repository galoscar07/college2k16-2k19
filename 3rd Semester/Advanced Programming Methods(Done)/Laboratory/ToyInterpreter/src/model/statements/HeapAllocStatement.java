package model.statements;

import model.ProgramState;
import model.expressions.Expression;

public class HeapAllocStatement implements Statement {
    private String varName;
    private Expression exp;

    public HeapAllocStatement(String var, Expression e) {
        varName = var;
        exp = e;
    }

    @Override
    public ProgramState execute(ProgramState prgState) {
        int val = exp.eval(prgState.getSymbolTable(), prgState.getHeap());
        prgState.getSymbolTable().add(varName, prgState.getHeap().put(val));
        return null;
    }

    @Override
    public String toString() {
        return "new(" + varName + ',' + exp + ")";
    }

}
