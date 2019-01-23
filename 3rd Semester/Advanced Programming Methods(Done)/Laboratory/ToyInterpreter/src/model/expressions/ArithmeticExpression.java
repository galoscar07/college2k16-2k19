package model.expressions;

import model.containers.IDictionary;
import model.containers.IHeap;
import model.exceptions.DivisionByZeroException;
import model.exceptions.UnknownOperatorException;

public class ArithmeticExpression implements Expression {
    private char op;
    private Expression l, r;

    public ArithmeticExpression(Expression l1, char o1, Expression r1) {
        op = o1;
        l = l1;
        r = r1;
    }

    public int eval(IDictionary<String, Integer> st, IHeap<Integer, Integer> h) {
        int a, b;
        a = l.eval(st, h);
        b = r.eval(st, h);
        switch (op) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '/':
                if (b == 0)
                    throw new DivisionByZeroException("Division by 0.");
                return a / b;
            case '*':
                return a * b;
            default:
                throw new UnknownOperatorException("Unknown operator.");
        }
    }

    @Override
    public String toString() {
        return l.toString() + op + r.toString();
    }
}
