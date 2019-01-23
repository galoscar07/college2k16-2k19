package domain.statements.ConditionalStatements;

import domain.PrgState;
import domain.exp.ArithExp;
import domain.exp.Exp;
import domain.statements.IStmt;

public class SwitchStmt implements IStmt{
    private Exp cond;
    private Exp expCase1;
    private Exp expCase2;
    private IStmt case1;
    private IStmt case2;
    private IStmt defaultCase;

    public SwitchStmt(Exp cond, Exp expCase1, Exp expCase2, IStmt case1, IStmt case2, IStmt defaultCase){
        this.cond = cond;
        this.expCase1 = expCase1;
        this.expCase2 = expCase2;
        this.case1 = case1;
        this.case2 = case2;
        this.defaultCase = defaultCase;
    }

    @Override
    public String toString() {
        return "SWITCH(" + cond.toString() + ") \n" + " case " + expCase1.toString() + ": " + case1.toString()
                + "\n case " + expCase2.toString() + ": " + case2.toString() + "\n default: " + defaultCase.toString();
    }

    @Override
    public PrgState execute(PrgState state){
        Exp difSwitch1 = new ArithExp('-',cond,expCase2);
        Exp difSwitch2 = new ArithExp('-',cond,expCase1);
        IStmt ifSwitch = new IfStmt(difSwitch2, defaultCase, case1);
        IStmt switchStmt = new IfStmt(difSwitch1, ifSwitch, case2);
        state.getExeStack().push(switchStmt);
        return state;
    }
}
