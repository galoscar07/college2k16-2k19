package model.expressions;

import model.containers.IDictionary;
import model.containers.IHeap;

public class ConstExpression implements Expression {
    private int val;

    public ConstExpression(int a) {
        val = a;
    }

    @Override
    public String toString() {
        return "" + val;
    }

    @Override
    public int eval(IDictionary<String, Integer> st, IHeap<Integer, Integer> heap) {
        return val;
    }
}