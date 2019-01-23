package Model.Statements.Barrier;

import Model.Statements.IStmt;
import Model.Utils.MyException;
import Model.Utils.PrgState;

public class awaitStmt implements IStmt {
    private String var;

    public awaitStmt(String var){
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        if(null == state.getSymTable().lookup(var)){
            throw new MyException("Unknown variable!");
        }

        int foundIndex = state.getSymTable().lookup(var);

        if(null == state.getBarrier().lookup(foundIndex)){
            throw new MyException("Unknown variable!\n");
        }

        synchronized (state.getBarrier()){
            if(state.getBarrier().lookup(foundIndex).getFirst().size() == state.getBarrier().lookup(foundIndex).getSecond()){
                return null;
            }
            if(state.getBarrier().lookup(foundIndex).getFirst().isInList(state.getId())){
                state.getStk().push(this);
            }
            else{
                state.getBarrier().lookup(foundIndex).getFirst().add(state.getId());
                state.getStk().push(this);
            }
        }
        return null;
    }

    public String toString(){
        String rez = "";

        rez = rez + "await(" + var + ")";
        return rez;
    }
}
