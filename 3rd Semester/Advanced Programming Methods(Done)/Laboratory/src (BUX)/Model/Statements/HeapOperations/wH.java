package Model.Statements.HeapOperations;

import Exceptions.MyControllerException;
import Exceptions.MyDictionaryException;
import Exceptions.MyStmtException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Statements.IStmt;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;


public class wH implements IStmt
{
    private String Id;
    private Exp value;

    public wH(String Id, Exp value)
    {
        this.Id=Id;
        this.value=value;
    }


    public PrgState execute(PrgState state) throws MyControllerException {
        MyIHeap<Integer> heap = state.getHeap();
        MyIDictionary<String, Integer> symTbl = state.getSymTable();
        try {
            int id = symTbl.lookup(Id);
            int val = value.eval(symTbl, heap);
            if (heap.get(id) == null)
                heap.alloc(val);
            else
                heap.update(id,val);
        } catch (MyStmtException e) {
            throw new MyControllerException(e);

        } catch (MyDictionaryException e) {
            throw new MyControllerException(e);
        }

        return null;
    }

    public String toString() {
        return "wH("+Id+","+value.toString()+")";
    }
}
