package Model;
import Exceptions.MyControllerException;
import Exceptions.MyDictionaryException;
import Exceptions.MyStackException;
import Exceptions.MyStmtExecException;
import Model.Utils.*;
import Model.Statements.IStmt;

import java.io.Serializable;

public class PrgState implements Serializable {
    private MyIStack<IStmt> exeStack;
    private MyIDictionary<String, Integer> symTable;
    private MyIList<Integer> out;
    private IStmt originalProgram;
    private IFileTable<Tuple> fileTbl;
    private MyIHeap<Integer> heap;
    private int id;
    private ILockTable lock;
    private ILatch<Integer,Integer> latch;

    public PrgState(MyIStack<IStmt> exeStack, MyIDictionary<String, Integer> symTable, MyIList<Integer> out, IStmt prg,
                    IFileTable<Tuple> fileT,MyIHeap<Integer> heap,ILockTable lock ,ILatch<Integer,Integer> l, int id)
    {
        this.exeStack = exeStack;
        this.symTable = symTable;
        this.out = out;
        this.originalProgram = prg;
        this.fileTbl=fileT;
        this.heap=heap;
        this.id=id;
        this.exeStack.push(originalProgram);
        this.lock=lock;
        this.latch=l;
    }

    public MyIStack<IStmt> getStk() {
        return exeStack;
    }

    public MyIDictionary<String, Integer> getSymTable() {
        return symTable;
    }

    public MyIList<Integer> getOut() {
        return out;
    }

    public IFileTable<Tuple> getFT() {return fileTbl;}

    public MyIHeap<Integer> getHeap(){return heap;}

    public IStmt getOriginalProgram(){return originalProgram;}

    public ILockTable getLockTable() {
        return lock;
    }

    public ILatch<Integer,Integer> getLatch(){return this.latch;}

    public boolean isNotCompleted()  {
        return !exeStack.getStk().empty();
    }

    public PrgState oneStep() throws MyStackException, MyControllerException, MyDictionaryException {
        if(exeStack.getStk().empty())
            throw new MyStackException("Empty Stack!") ;
        IStmt crtStmt = exeStack.getStk().pop();
        return crtStmt.execute(this);
    }

    public int getId(){return id;}

    public String toString(){
        return "Id="+id+"\nExeStack:\n"+this.exeStack.toString()+"\nHeap:\n"+this.heap.toString()+
                "\nSym Table:\n"+symTable.toString()+"\n"+"Lock Table:\n"+lock.toString();
    }



}


