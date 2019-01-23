package domain.statements.IncDecStatements;

import domain.PrgState;
import domain.exp.ArithExp;
import domain.exp.ConstExp;
import domain.exp.VarExp;
import domain.statements.AssignStmt;
import domain.statements.IStmt;

public class IncStmt implements IStmt {
    private String varName;

    public IncStmt(String varName){
        this.varName = varName;
    }

    @Override
    public String toString(){
        return "INC(" + this.varName + ")";
    }

    @Override
    public PrgState execute(PrgState state){
        state.getExeStack().push(new AssignStmt(this.varName, new ArithExp('+',new VarExp(varName),new ConstExp(1))));
        return null;
    }
}
