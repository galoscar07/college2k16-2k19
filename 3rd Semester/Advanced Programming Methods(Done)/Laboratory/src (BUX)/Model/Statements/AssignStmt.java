package Model.Statements;

import Exceptions.*;
import Model.*;
import Model.Expressions.Exp;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;
import Model.Utils.MyIStack;

public class AssignStmt implements IStmt{
    String id;
    Exp exp;
    public AssignStmt(String id, Exp exp){
        this.id=id;
        this.exp=exp;
    }
    public String toString(){ return id+"="+exp;
    }
    public PrgState execute(PrgState state) throws MyControllerException {
        MyIStack<IStmt> stk=state.getStk();
        MyIDictionary<String,Integer> symTbl= state.getSymTable();
        MyIHeap<Integer> heap=state.getHeap();
        try {
            int val = exp.eval(symTbl,heap);
            if (symTbl.isDefined(id)==1)
                symTbl.update(id, val);
            else
                symTbl.put(id,val);
            return null;
        }
        catch (MyStmtException e){
            throw new MyControllerException(e);
        }
        catch (DivisionByZeroException e){
            throw new MyControllerException(e);
        }
    }

}
