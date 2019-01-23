package model;

import exception.*;

import java.io.IOException;

public class WhileStmt implements IStmt {
    private Exp exp;
    private IStmt stmt;
    public WhileStmt(Exp exp, IStmt stmt) {
        this.exp = exp;
        this.stmt = stmt;
    }
    @Override
    public PrgState execute(PrgState state) throws UnknownComparisonExpression, IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException {
        MyIStack<IStmt> exeStack = state.getExeStack();
        if(exp.eval(state.getSymTable(), state.getHeap()) != 0) {
            exeStack.push(this);
            exeStack.push(stmt);
        }
        return null;
    }

    @Override
    public String toString() {
        return "while(" + this.exp.toString() + ") do " + this.stmt.toString() + " end";
    }
}
