package Model.Statements;

import Exceptions.MyControllerException;
import Model.Utils.MyIStack;
import Model.PrgState;

public class CompStmt implements IStmt
{
    IStmt first;
    IStmt snd;
    public CompStmt(IStmt first,IStmt snd){
        this.first=first;
        this.snd=snd;
    }

    public String toString() {
        return first+";"+snd;
    }
    public PrgState execute(PrgState state)throws MyControllerException
    {
        MyIStack<IStmt> stk = state.getStk();
        stk.push(snd);
        stk.push(first);
        return null;
    }
}

