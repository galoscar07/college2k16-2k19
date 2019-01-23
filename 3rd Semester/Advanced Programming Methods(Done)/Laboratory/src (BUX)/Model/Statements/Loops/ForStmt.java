package Model.Statements.Loops;

import Model.Expressions.Boolean;
import Model.Expressions.Exp;
import Model.Expressions.VarExp;
import Model.PrgState;
import Model.Statements.AssignStmt;
import Model.Statements.CompStmt;
import Model.Statements.IStmt;

public class ForStmt implements IStmt {
    private Exp e1,e2,e3;
    private IStmt stmt;

    public ForStmt(Exp e1, Exp e2, Exp e3,IStmt stmt){
        this.e1 = e1;
        this.e2 = e2;
        this.e3 = e3;
        this.stmt = stmt;
    }

    @Override
    public PrgState execute(PrgState state) {
        IStmt stmt1  = new AssignStmt("v", e1);
        IStmt whileStmt = new CompStmt(stmt1, new While(new Boolean(new VarExp("v"), e2, ">"), new CompStmt(this.stmt,
                new AssignStmt("v", e3))));
        state.getStk().push(whileStmt);
        return null;
    }

    public String toString(){
        String rez = "";

        rez = rez + "for(v = " + e1.toString() + "; v < " + e2.toString() + "; v  = " + e3.toString() + "){\n\t" +
                this.stmt.toString() + "\n}";

        return rez;
    }
}