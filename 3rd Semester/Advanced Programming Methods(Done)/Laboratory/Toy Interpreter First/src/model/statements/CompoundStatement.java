package model.statements;

import model.ProgramState;

public class CompoundStatement implements Statement {
    private Statement first, second;

    public CompoundStatement(Statement f, Statement s) {
        first = f;
        second = s;
    }

    @Override
    public ProgramState execute(ProgramState ps) {
        ps.getExecStack().push(second);
        ps.getExecStack().push(first);
        return null;
    }

    @Override
    public String toString() {
        return "(" + first + "," + second + ")";
    }
}
