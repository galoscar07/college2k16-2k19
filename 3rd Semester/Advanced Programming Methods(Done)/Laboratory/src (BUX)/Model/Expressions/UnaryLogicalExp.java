package Model.Expressions;

import Exceptions.MyStmtException;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;

public class UnaryLogicalExp extends Exp {
    private final Exp exp;
    private final String operator;

    public UnaryLogicalExp(Exp exp, String operator) {
        this.exp = exp;
        this.operator = operator;
    }

    @Override
    public int eval(MyIDictionary<String, Integer> symbols, MyIHeap<Integer> heap) {

        Integer result = null;
        try {
            result = exp.eval(symbols, heap);
        } catch (MyStmtException e) {
            e.printStackTrace();
        }
        switch (operator) {
            case "!":
                return 1 - result;
        }
        return 0;
    }

    @Override
    public String toString() {
        return "!(" + exp.toString() + ")";
    }
}