package model.expressions;

import model.containers.IDictionary;
import model.containers.IHeap;
import model.exceptions.UnknownOperatorException;

public class BooleanExpression implements Expression {
    private String op;
    private Expression l, r;

    public BooleanExpression(Expression l1, String o1, Expression r1) {
        op = o1;
        l = l1;
        r = r1;
    }

    public int eval(IDictionary<String, Integer> st, IHeap<Integer, Integer> h) {
        int a, b;
        a = l.eval(st, h);
        b = r.eval(st, h);
        switch (op) {
            case "<":
                if (a < b) return 1;
                return 0;
            case "<=":
                if (a <= b) return 1;
                return 0;
            case "==":
                if (a == b) return 1;
                return 0;
            case "!=":
                if (a != b) return 1;
                return 0;
            case ">":
                if (a > b) return 1;
                return 0;
            case ">=":
                if (a >= b) return 1;
                return 0;
            default:
                throw new UnknownOperatorException("Unknown operator.");
        }
    }

    @Override
    public String toString() {
        return l.toString() + op + r.toString();
    }
}
