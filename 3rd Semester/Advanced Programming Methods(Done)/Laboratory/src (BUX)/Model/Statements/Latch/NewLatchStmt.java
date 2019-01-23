package Model.Statements.Latch;

import Exceptions.MyControllerException;
import Exceptions.MyException;
import Exceptions.MyStmtException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Statements.IStmt;

public class NewLatchStmt implements IStmt {

    private String var;
    private Exp exp;

    public NewLatchStmt(String var, Exp exp){
        this.var = var;
        this.exp = exp;
    }

    @Override
    public PrgState execute(PrgState state) throws MyControllerException {
        synchronized (state.getLatch())
        {
            int val;
            try{
                val = exp.eval(state.getSymTable(), state.getHeap());
            }catch (MyStmtException e)
            {
                throw new MyControllerException(e);
            }
            if(state.getSymTable().isDefined(var) == 1)
                state.getSymTable().put(var, (Integer) state.getLatch().add(val));
            else
                state.getSymTable().put(var, (Integer) state.getLatch().add(val));
        }

        return null;
    }

    @Override
    public String toString() {
        return "newLatch(" + var + ", " + exp.toString() + ")";
    }
}
