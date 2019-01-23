package Model.Expressions;

import Exceptions.MyStmtException;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;

import java.util.Objects;

public class RelationalExp extends Exp {

    private final Exp exp1;
    private final Exp exp2;
    private final String operator;

    public RelationalExp(Exp exp1, Exp exp2, String operator) {
        this.exp1 = exp1;
        this.exp2 = exp2;
        this.operator = operator;
    }

    @Override
    public int eval(MyIDictionary<String, Integer> symbols, MyIHeap<Integer> heap)  {

        Integer result1 = null;
        try {
            result1 = exp1.eval(symbols, heap);
        } catch (MyStmtException e) {
            e.printStackTrace();
        }
        Integer result2 = null;
        try {
            result2 = exp2.eval(symbols, heap);
        } catch (MyStmtException e) {
            e.printStackTrace();
        }
        switch (operator) {
            case "<":
                return (result1 < result2) ? 1 : 0;
            case "<=":
                return (result1 <= result2) ? 1 : 0;
            case "==":
                return (Objects.equals(result1, result2)) ? 1 : 0;
            case "!=":
                return (!Objects.equals(result1, result2)) ? 1 : 0;
            case ">":
                return (result1 > result2) ? 1 : 0;
            case ">=":
                return (result1 >= result2) ? 1 : 0;

        }
        return 0;
    }

    @Override
    public String toString() {
        return "(" + exp1.toString() + " " + operator + " " + exp2.toString() + ")";
    }
}
