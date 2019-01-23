package Model.Statements;
import Exceptions.MyControllerException;
import Exceptions.MyStmtException;
import Model.Expressions.Exp;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;
import Model.Utils.MyIStack;
import Model.PrgState;

public class IfStmt implements IStmt{
    Exp exp;
    IStmt thenS;
    IStmt elseS;
    public IfStmt(Exp e, IStmt t, IStmt el) {this.exp=e; this.thenS=t;this.elseS=el;}
    public String toString(){ return "IF("+ exp.toString()+") THEN(" +thenS.toString()
            +")ELSE("+elseS.toString()+")";}
    public PrgState execute(PrgState state) throws MyControllerException {
        MyIStack<IStmt> stk=state.getStk();
        MyIDictionary<String, Integer> symTbl = state.getSymTable();
        MyIHeap<Integer> heap=state.getHeap();
        try {
            if (exp.eval(symTbl,heap) > 0)
                stk.push(thenS);
            else
                stk.push(elseS);
            return null;
        }
        catch(MyStmtException e){
            throw new MyControllerException(e);
        }
    }
}
