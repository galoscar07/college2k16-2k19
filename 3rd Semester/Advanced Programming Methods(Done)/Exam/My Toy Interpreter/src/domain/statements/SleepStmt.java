package domain.statements;

import domain.adt.MyIHeap;
import domain.PrgState;
import domain.adt.MyIDictionary;
import domain.adt.MyIStack;
import domain.exp.ConstExp;
import domain.exp.Exp;
import exception.DivideByZeroException;
import exception.UnknownComparisonExpression;
import exception.UnknownVariableException;

public class SleepStmt implements IStmt{
    private Exp number;

    public SleepStmt(Exp number){
        this.number = number;
    }

    @Override
    public String toString(){
        return "Sleep( " + this.number + " )";
    }

    @Override
    public PrgState execute(PrgState state){
        MyIStack<IStmt> localStack = state.getExeStack();
        MyIDictionary<String,Integer> localSym = state.getSymTable();
        MyIHeap<Integer> localHeap = state.getHeap();

        Integer nr = null;
        try{
            nr = this.number.eval(localSym,localHeap);
        } catch (UnknownVariableException e) {
            e.printStackTrace();
        } catch (DivideByZeroException e) {
            e.printStackTrace();
        } catch (UnknownComparisonExpression e) {
            e.printStackTrace();
        }
        Integer nr1 = nr;
        if(nr > 0){
            nr1 = nr - 1;
            localStack.push(new SleepStmt(new ConstExp(nr1)));
        }
        return null;
    }

}
