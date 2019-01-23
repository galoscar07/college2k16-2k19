package Model.Statements;
import Model.Expressions.ArithExp;
import Model.Expressions.ConstExp;
import Model.Expressions.VarExp;
import Model.PrgState;
import Model.Statements.AssignStmt;
import Model.Statements.IStmt;

public class DecrStmt implements IStmt {

    private String mVarName;

    public DecrStmt(String varName) {
        mVarName = varName;
    }

    public String getVarName(){
        return mVarName;
    }

    @Override
    public String toString() {
        return "DECR("+mVarName+")";
    }

    @Override
    public PrgState execute(PrgState state)
    {

        state.getStk().push(new AssignStmt(mVarName,new ArithExp(2, new VarExp(mVarName) , new ConstExp(1) ) ));
        return null;
    }



}
