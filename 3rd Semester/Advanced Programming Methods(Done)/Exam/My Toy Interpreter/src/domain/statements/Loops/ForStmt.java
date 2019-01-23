package domain.statements.Loops;

import domain.PrgState;
import domain.exp.*;
import domain.statements.AssignStmt;
import domain.statements.CompStmt;
import domain.statements.IStmt;

public class ForStmt implements IStmt {
    private Exp e1,e2,e3;
    private IStmt stmt;

    public ForStmt(Exp e1, Exp e2, Exp e3, IStmt stmt){
        this.e1 = e1;
        this.e2 = e2;
        this.e3 = e3;
        this.stmt = stmt;
    }

    @Override
    public PrgState execute(PrgState state) {
        IStmt stmt1 = new AssignStmt("v",e1);
        IStmt stmt2 = new AssignStmt("v",new ArithExp('-', new VarExp("v"), e3));
        IStmt whileStmt = new CompStmt(stmt1, new WhileStmt(new BoolExp(">",new VarExp("v"),e2), new CompStmt(this.stmt,stmt2)));
        state.getExeStack().push(whileStmt);
        return null;
    }

    @Override
    public String toString(){
        String rez = "";
        rez = rez + "for( v = " + e1.toString() + "; v < " + e2.toString() + "; v  -= " + e3.toString() + "){\n\t" +
                this.stmt.toString() + "\n}";
        return rez;
    }

}
