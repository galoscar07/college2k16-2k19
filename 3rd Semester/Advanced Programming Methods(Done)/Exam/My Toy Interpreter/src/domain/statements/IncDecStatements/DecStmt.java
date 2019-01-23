package domain.statements.IncDecStatements;

import domain.PrgState;
import domain.exp.ArithExp;
import domain.exp.ConstExp;
import domain.exp.VarExp;
import domain.statements.AssignStmt;
import domain.statements.IStmt;

public class DecStmt implements IStmt {
    private String varName;

    public DecStmt(String varName){
        this.varName = varName;
    }

    @Override
    public String toString(){
        return "DEC(" + this.varName + ")";
    }

    @Override
    public PrgState execute(PrgState state){
        state.getExeStack().push(new AssignStmt(this.varName, new ArithExp('-',new VarExp(varName),new ConstExp(1))));
        return null;
    }
}
