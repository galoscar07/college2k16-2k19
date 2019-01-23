package model;

import exception.DivideByZeroException;
import exception.UnknownComparisonExpression;
import exception.UnknownVariableException;

public abstract class Exp {
    abstract public int eval(MyIDictionary<String, Integer> symTable, MyIHeap<Integer> heap) throws DivideByZeroException, UnknownVariableException, UnknownComparisonExpression;
    @Override
    abstract public String toString();
}
