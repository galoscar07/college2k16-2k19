package Model.Statements.Barrier;

import Model.Collections.MyIList;
import Model.Collections.MyList;
import Model.Collections.Tuple;
import Model.Expressions.Exp;
import Model.Statements.IStmt;
import Model.Utils.MyException;
import Model.Utils.PrgState;

import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public class newBarrierStmt implements IStmt {
    private String var;
    private Exp exp;
    private Integer newFreeLocation = -1;

    public newBarrierStmt(String var, Exp exp){
        this.var = var;
        this.exp = exp;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        int number = this.exp.eval(state.getSymTable(), state.getHeapTable());
        synchronized (state.getBarrier()){
            MyIList<Integer> empty = new MyList<>();
            Tuple<MyIList<Integer>, Integer> param = new Tuple<MyIList<Integer>, Integer>(empty, number);
            state.getBarrier().add(newFreeLocation, param);
            synchronized (state.getSymTable()){
                state.getSymTable().add(var, newFreeLocation);
            }
        }

        return null;
    }

    public String toString(){
        String rez = "";

        rez = rez + "newBarrier(" + this.var + " , " + this.exp.toString() + ")";
        return rez;
    }
}
