package Model.Statements.Lock;

import Exceptions.MyControllerException;
import Exceptions.MyDictionaryException;
import Model.PrgState;
import Model.Statements.IStmt;
import Model.Utils.ILockTable;
import Model.Utils.MyIDictionary;


public class unlock implements IStmt {

    private String var;

    public unlock(String var)
    {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws MyControllerException {
        MyIDictionary<String, Integer> dict = state.getSymTable();
        ILockTable ltable = state.getLockTable();

        try{
            int foundIndex = dict.lookup(var);
            if(ltable.get(foundIndex) == state.getId())
                ltable.update(foundIndex, -1);
        }catch (MyDictionaryException e)
        {
            throw new MyControllerException(e);
        }
        catch (Exception e)
        {
            throw new MyControllerException(e.toString());
        }

        return state;
    }

    @Override
    public String toString() {
        return "unlock(" + var + ")";
    }
}

