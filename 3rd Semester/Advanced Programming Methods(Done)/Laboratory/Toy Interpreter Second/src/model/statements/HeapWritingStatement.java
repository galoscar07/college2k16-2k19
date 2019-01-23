package model.statements;

import model.ProgramState;
import model.containers.IDictionary;
import model.containers.IHeap;
import model.exceptions.NotFoundException;
import model.expressions.Expression;

public class HeapWritingStatement implements Statement {
    private String var_name;
    private Expression expr;

    public HeapWritingStatement(String v, Expression e) {
        var_name = v;
        expr = e;
    }

    @Override
    public ProgramState execute(ProgramState prgState) {
        IHeap<Integer, Integer> heap = prgState.getHeap();
        IDictionary<String, Integer> symTable = prgState.getSymbolTable();
        int addr;
        if (symTable.contains(var_name)) {
            addr = symTable.get(var_name);
        } else {
            throw new NotFoundException("Variable not found");
        }
        if (heap.contains(addr)) {
            heap.update(addr, expr.eval(symTable, heap));
        } else {
            throw new NotFoundException("Invalid address");
        }
        return null;
    }

    @Override
    public String toString() {
        return "wH(" + var_name + "," + expr + ")";
    }
}
