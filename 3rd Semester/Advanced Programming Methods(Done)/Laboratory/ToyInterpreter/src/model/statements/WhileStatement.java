package model.statements;

import model.ProgramState;
import model.expressions.Expression;

public class WhileStatement implements Statement {
    private Statement st;
    private Expression exp;

    public WhileStatement(Expression e, Statement s) {
        exp = e;
        st = s;
    }

    @Override
    public ProgramState execute(ProgramState ps) {
        int a = exp.eval(ps.getSymbolTable(), ps.getHeap());
        if (a != 0) {
            ps.getExecStack().push(this);
            ps.getExecStack().push(st);
        }
        return null;
    }

    @Override
    public String toString() {
        return "(while(" + exp + ") " + st + ")";
    }
}
