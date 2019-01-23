package Model.Statements.Latch;

import Exceptions.MyControllerException;
import Exceptions.MyDictionaryException;
import Model.PrgState;
import Model.Statements.IStmt;

public class AwaitStmt implements IStmt {
    private String var;

    public AwaitStmt(String v) {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws MyControllerException {

        Integer val;
        if (state.getSymTable().isDefined(var) == 1) {
            try {
                val = (Integer) state.getLatch().get(state.getSymTable().lookup(var));
            } catch (MyDictionaryException e) {
                throw new MyControllerException(e);
            } catch (Exception e) {
                throw new MyControllerException(e.toString());
            }
            if (val != 0)
                state.getStk().push(this);
        } else
            throw new MyControllerException("No such key!");

        return null;
    }

    @Override
    public String toString() {
        return "await(" + var + ")";
    }

}
