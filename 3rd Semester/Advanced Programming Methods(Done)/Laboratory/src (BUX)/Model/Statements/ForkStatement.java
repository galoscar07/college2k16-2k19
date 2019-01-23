package Model.Statements;

import Exceptions.MyControllerException;
import Exceptions.MyStackException;
import Model.PrgState;
import Model.Utils.*;

import java.util.Collections;
import java.util.Map;
import java.util.stream.Collectors;


public class ForkStatement implements IStmt {
    private IStmt stmt;
    public ForkStatement(IStmt statement){this.stmt=statement;}
    public PrgState execute(PrgState state) throws MyControllerException {
        MyIDictionary<String,Integer> symTbl=state.getSymTable();
        MyIHeap<Integer> heap=state.getHeap();
        MyIList<Integer> out=state.getOut();
        int id=state.getId();
        IFileTable<Tuple> ft=state.getFT();
        ILockTable lock=state.getLockTable();
        ILatch<Integer,Integer> latch=new Latch<>();


        MyIStack<IStmt> stk3=new MyStack<>();
        MyIDictionary<String,Integer> symTbl3=new MyDictionary<>();
        symTbl3.setMap(state.getSymTable().getContent().entrySet().stream().collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue)));
        PrgState state3=new PrgState(stk3,symTbl3,out,stmt,ft,heap,lock,latch,id*10);

        return state3;

    }
    public String toString() {
        return "fork("+stmt.toString()+")";
    }
}
