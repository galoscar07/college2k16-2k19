package Model.Statements.HeapOperations;

import Exceptions.MyControllerException;
import Exceptions.MyStmtException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Statements.IStmt;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;

public class NewStmt implements IStmt {
    private String Id;
    private Exp value;

    public NewStmt(String Id, Exp value){
        this.Id=Id;
        this.value=value;
    }

    public PrgState execute(PrgState state) throws MyControllerException {
        MyIDictionary<String,Integer> symTbl=state.getSymTable();
        MyIHeap<Integer> heap=state.getHeap();
        try{
            int val=value.eval(symTbl,heap);
            heap.alloc(val);
            int adr=heap.getCurr()-1;
            if(symTbl.isDefined(Id)==0)
                symTbl.put(Id,adr);
            else
                symTbl.update(Id,adr);

        }
        catch (MyStmtException e)
        {
            throw new MyControllerException(e);
        }
        return null;
    }


    public String toString() {
        return "new("+Id+","+value.toString()+")";
    }
}
