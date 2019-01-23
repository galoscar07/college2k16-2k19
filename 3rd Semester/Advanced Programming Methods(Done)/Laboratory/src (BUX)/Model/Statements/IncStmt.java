package Model.Statements;

import Model.Expressions.ArithExp;
import Model.Expressions.ConstExp;
import Model.Expressions.VarExp;
import Model.PrgState;

public class IncStmt implements IStmt {

    private String mVarName;

    public IncStmt(String varName) {
        mVarName = varName;
    }

    public String getVarName(){
        return mVarName;
    }

    @Override
    public String toString() {
        return "INC("+mVarName+")";
    }

    @Override
    public PrgState execute(PrgState state)
    {

        state.getStk().push(new AssignStmt(mVarName,new ArithExp(1, new VarExp(mVarName) , new ConstExp(1) ) ));
        return null;
    }



}
