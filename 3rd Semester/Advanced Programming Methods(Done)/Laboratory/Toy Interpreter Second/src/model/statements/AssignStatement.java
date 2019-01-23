package model.statements;

import model.ProgramState;
import model.containers.IDictionary;
import model.containers.IHeap;
import model.expressions.Expression;

public class AssignStatement implements Statement {
    private String varName;
    private Expression value;

    public AssignStatement(String n, Expression v) {
        varName = n;
        value = v;
    }

    @Override
    public ProgramState execute(ProgramState ps) {
        IDictionary<String, Integer> st = ps.getSymbolTable();
        IHeap<Integer, Integer> h = ps.getHeap();
        int e = value.eval(st, h);
        if (st.contains(varName)) {
            st.update(varName, e);
        } else {
            st.add(varName, e);
        }
        return null;
    }

    @Override
    public String toString() {
        return varName + "=" + value;
    }
}
