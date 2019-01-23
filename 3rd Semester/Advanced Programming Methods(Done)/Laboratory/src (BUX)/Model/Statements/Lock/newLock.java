package Model.Statements.Lock;

import Exceptions.MyControllerException;
import Model.PrgState;
import Model.Statements.IStmt;
import Model.Utils.ILockTable;
import Model.Utils.MyIDictionary;


public class newLock implements IStmt {
    private String var;

    public newLock(String var)
    {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws MyControllerException {
        MyIDictionary<String, Integer> dict = state.getSymTable();
        ILockTable ltable = state.getLockTable();

        int newFreeLocation = ltable.add(-1);
        dict.put(var, newFreeLocation);

        return null;

    }

    @Override
    public String toString() {
        return "newLock(" + var + ")";
    }
}

