package model.statements;

import model.ProgramState;
import model.containers.IDictionary;
import model.containers.IHeap;
import model.expressions.Expression;

public class PrintStatement implements Statement {
    private Expression expr;

    public PrintStatement(Expression e) {
        expr = e;
    }

    @Override
    public ProgramState execute(ProgramState ps) {
        IDictionary<String, Integer> st = ps.getSymbolTable();
        IHeap<Integer, Integer> h = ps.getHeap();
        int e = expr.eval(st, h);
        ps.getList().add(e);
        return null;
    }

    @Override
    public String toString() {
        return "Print(" + expr + ")";
    }
}
