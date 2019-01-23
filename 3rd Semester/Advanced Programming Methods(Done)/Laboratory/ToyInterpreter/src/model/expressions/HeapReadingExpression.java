package model.expressions;

import model.containers.IDictionary;
import model.containers.IHeap;
import model.exceptions.NotFoundException;

public class HeapReadingExpression implements Expression {
    private String var;

    public HeapReadingExpression(String v) {
        var = v;
    }

    @Override
    public int eval(IDictionary<String, Integer> symbolTable, IHeap<Integer, Integer> heap) {
        if (!symbolTable.contains(var))
            throw new NotFoundException("Variable does not exist");
        Integer value = symbolTable.get(var);
        if (!heap.contains(value))
            throw new NotFoundException("Invalid address");
        return heap.get(value);
    }

    @Override
    public String toString() {
        return "rH(" + var + ")";
    }
}