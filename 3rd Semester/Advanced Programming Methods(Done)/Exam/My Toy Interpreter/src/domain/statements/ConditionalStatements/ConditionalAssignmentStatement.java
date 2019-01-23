package domain.statements.ConditionalStatements;

import domain.PrgState;
import domain.exp.Exp;
import domain.statements.AssignStmt;
import domain.statements.IStmt;

public class ConditionalAssignmentStatement implements IStmt {

    private String id;
    private Exp exp1;
    private Exp exp2;
    private Exp exp3;

    public ConditionalAssignmentStatement(String id, Exp exp1, Exp exp2, Exp exp3){
        this.id = id;
        this.exp1 = exp1;
        this.exp2 = exp2;
        this.exp3 = exp3;
    }

    @Override
    public String toString(){
        return "" + id + " = " + exp1.toString() + " ? " + exp2.toString() + " : " + exp3.toString();
    }

    @Override
    public PrgState execute(PrgState state) {
        IStmt statement1 = new AssignStmt(this.id,this.exp2);
        IStmt statement2 = new AssignStmt(this.id,this.exp3);
        IStmt ifstatement = new IfStmt(this.exp1,statement1,statement2);
        state.getExeStack().push(ifstatement);
        return null;
    }
}

