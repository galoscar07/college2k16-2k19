package Model.Statements.Loops;

import Exceptions.MyControllerException;
import Exceptions.MyDictionaryException;
import Exceptions.MyStmtException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Statements.IStmt;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;
import Model.Utils.MyIStack;
import Model.Utils.MyStack;


public class While implements IStmt {
    private Exp exp;
    private IStmt stmt;

    public While(Exp expression,IStmt statement){this.exp=expression;this.stmt=statement;}


    public PrgState execute(PrgState state) throws MyControllerException, MyDictionaryException {
        MyIStack<IStmt> stk=state.getStk();
        MyIDictionary<String,Integer> symTbl=state.getSymTable();
        MyIHeap<Integer> heap=state.getHeap();
        if (stk.getStk().empty()) {
            try {
                while (exp.eval(symTbl, heap) >= 1) {
                    stmt.execute(state);
                    while (!stk.getStk().empty()) {
                        IStmt st = stk.pop();
                        System.out.println(st.toString() + " ");
                        st.execute(state);
                    }
                }
            } catch (MyStmtException e) {
                throw new MyControllerException(e);
            }
        }
        else {
            IStmt last=stk.getStk().peek();
            try {
                while (exp.eval(symTbl, heap) >= 1) {
                    stmt.execute(state);
                    while (stk.pop() != last) {
                        IStmt st = stk.pop();
                        System.out.println(st.toString() + " ");
                        st.execute(state);
                    }
                }
            } catch (MyStmtException e) {
                throw new MyControllerException(e);
            }
        }
        return null;
    }


    public String toString() {
        return "while("+exp.toString()+stmt.toString()+")";}
}
