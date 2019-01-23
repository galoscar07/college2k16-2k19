package model.expressions;

import model.containers.IDictionary;
import model.containers.IHeap;
import model.exceptions.NotFoundException;

public class VariableExpression implements Expression {
    private String varName;

    public VariableExpression(String n) {
        varName = n;
    }

    public int eval(IDictionary<String, Integer> st, IHeap<Integer, Integer> h) {
        if (st.contains(varName))
            return st.get(varName);
        else {
            throw new NotFoundException("Variable not found.");
        }
    }

    @Override
    public String toString() {
        return varName;
    }
}
