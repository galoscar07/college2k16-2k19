package Model.Statements.Latch;

import Exceptions.MyControllerException;
import Exceptions.MyDictionaryException;
import Exceptions.MyException;
import Model.PrgState;
import Model.Statements.IStmt;
import Model.Utils.MyDictionary;

public class CountDownStmt implements IStmt {
    private String varname;

    public CountDownStmt(String v){
        this.varname = v;
    }


    @Override
    public PrgState execute(PrgState state) throws MyControllerException {
        Object lock = new Object();
        if(state.getSymTable().isDefined(varname) == 1)
            synchronized (lock)
            {
                Integer val;
                try{
                    val = (Integer) state.getLatch().get(state.getSymTable().lookup(varname));
                    if(val > 0) {
                        Integer newVal = val - 1;
                        state.getLatch().update(state.getSymTable().lookup(varname), newVal);
                    }
                }catch (MyDictionaryException e)
                {
                    throw new MyControllerException(e);
                }
                catch (Exception e)
                {
                    throw new MyControllerException(e.toString());
                }



            }
        else
            throw new MyControllerException("No such key!");


        return null;
    }

    @Override
    public String toString() {
        return "countDown(" + varname + ")";
    }
}