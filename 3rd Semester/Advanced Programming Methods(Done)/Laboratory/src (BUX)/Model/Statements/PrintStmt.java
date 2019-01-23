package Model.Statements;

import Exceptions.MyControllerException;
import Exceptions.MyStmtException;
import Model.Expressions.Exp;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;
import Model.Utils.MyIList;
import Model.PrgState;

public class PrintStmt implements IStmt{
    Exp exp;
    public PrintStmt(Exp exp){this.exp=exp;}
    public String toString(){ return "print("+ exp+")";}
    public PrgState execute(PrgState state) throws MyControllerException {
        MyIList<Integer> out=state.getOut();
        MyIDictionary<String,Integer> symTbl = state.getSymTable();
        MyIHeap<Integer> heap=state.getHeap();
        try {
            out.add(exp.eval(symTbl,heap));
            return null;
        }
        catch(MyStmtException e){
            throw new MyControllerException(e);
        }
    }
}
