package Model.Statements.Lock;

import Exceptions.MyControllerException;

import Model.Statements.IStmt;
import Model.Utils.ILockTable;
import Model.Utils.MyIDictionary;
import Model.PrgState;
import Model.Utils.MyIStack;

public class lockStatement implements IStmt {
    private String var;

    public lockStatement(String var){
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws MyControllerException {
        MyIDictionary<String, Integer> dict = state.getSymTable();
        ILockTable lTable = state.getLockTable();
        MyIStack<IStmt> stk = state.getStk();

        try{
            int foundIndex = dict.lookup(var);
            if(lTable.get(foundIndex) == -1)
                lTable.update(foundIndex, state.getId());
            else
                stk.push(this);
        } catch (Exception e)
        {
            throw new MyControllerException(e.toString());
        }

        return null;


    }

    @Override
    public String toString() {
        return "lock(" + var + ")";
    }
}
