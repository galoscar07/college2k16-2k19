package Model.Statements;

import Exceptions.MyStmtException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Utils.MyIStack;

public class IfThenStatement implements IStmt {
    protected final Exp expression;
    protected final IStmt thenStatement;

    public IfThenStatement(Exp expression, IStmt thenStatement) {
        this.expression = expression;
        this.thenStatement = thenStatement;
    }

    @Override
    public String toString() {
        return "if " + expression.toString() +
                " then " + thenStatement.toString();
    }

    @Override
    public PrgState execute(PrgState state) {
        MyIStack<IStmt> stack = state.getStk();
        stack.push(new IfStmt(expression, thenStatement, new Skip()));
        return null;
    }


}