package View;

import Controller.Ctrl;
import Model.*;
import Model.Expressions.*;
import Model.Statements.HeapOperations.NewStmt;
import Model.Statements.HeapOperations.wH;
import Model.Statements.Latch.AwaitStmt;
import Model.Statements.Latch.CountDownStmt;
import Model.Statements.Latch.NewLatchStmt;
import Model.Statements.Lock.lockStatement;
import Model.Statements.Lock.newLock;
import Model.Statements.Lock.unlock;
import Model.Utils.*;
import Model.Statements.*;
import Repo.Repository;
import Repo.IRepo;
import View.Commands.ExitCommand;
import View.Commands.RunCommand;


import java.io.IOException;

public class  Interpreter {
    public static void main(String[] args) {

       /* MyIDictionary<String, Integer> symtab8 = new MyDictionary<String, Integer>();
        MyIStack<IStmt> stk8 = new MyStack<IStmt>();
        MyIList<Integer> out8 = new MyList<Integer>();
        IFileTable<Tuple> fileT8 = new FileTable<Tuple>();
        IStmt st8 = new CompStmt(new AssignStmt("v",new ConstExp(10)),new CompStmt(new NewStmt("a",
                new ConstExp(22)),new CompStmt(new ForkStatement(new CompStmt(new wH("a",
                new ConstExp(30)),new CompStmt(new AssignStmt("v",new ConstExp(32)),
                new CompStmt(new AssignStmt("a",new ConstExp(0)),new PrintStmt(new VarExp("v")))))),
                new CompStmt(new PrintStmt(new VarExp("v")),new AssignStmt("a",new ConstExp(20))))));
        MyIHeap<Integer> heap8 = new MyHeap<>();
        PrgState state8 = new PrgState(stk8, symtab8, out8, st8, fileT8,heap8,1);
        IRepo repo8 = null;
        try{
            repo8 = new Repository("D:\\ubb\\MAP\\lab2-modif2\\src\\fileState1.txt");
        }catch (IOException e)
        {
            System.out.println(e.toString());
        }
        Ctrl cont8=new Ctrl(repo8);



        MyIDictionary<String, Integer> symtab7 = new MyDictionary<String, Integer>();
        MyIStack<IStmt> stk7 = new MyStack<IStmt>();
        MyIList<Integer> out7 = new MyList<Integer>();
        IFileTable<Tuple> fileT7 = new FileTable<Tuple>();
        IStmt st7 = new ForkStatement(new CompStmt(new AssignStmt("a",new ConstExp(32)),new While(new Boolean(new VarExp("a"),
                new ConstExp(4),">"),new CompStmt(new PrintStmt(new VarExp("a")), new AssignStmt("a",
                new ArithExp(4,new VarExp("a"),new ConstExp(2)))))));
        MyIHeap<Integer> heap7 = new MyHeap<>();
        PrgState state7 = new PrgState(stk7, symtab7, out7, st7, fileT7,heap7,2);
        IRepo repo7 = null;
        try{
            repo7 = new Repository("D:\\ubb\\MAP\\lab2-modif2\\src\\fileState7.txt");
        }catch (IOException e)
        {
            System.out.println(e.toString());
        }
        Ctrl cont7=new Ctrl(repo7);

        MyIDictionary<String, Integer> symtab5 = new MyDictionary<String, Integer>();
        MyIStack<IStmt> stk5 = new MyStack<IStmt>();
        MyIList<Integer> out5 = new MyList<Integer>();
        IFileTable<Tuple> fileT5 = new FileTable<Tuple>();
        IStmt st5 = new CompStmt(new AssignStmt("v", new ConstExp(10)), new CompStmt(new NewStmt
                ("v", new ConstExp(20)), new CompStmt(new NewStmt("a", new ConstExp(22)), new
                CompStmt(new wH("a", new ConstExp(30)), new CompStmt(new PrintStmt
                (new VarExp("a")), new PrintStmt(new rH("a")))))));
        MyIHeap<Integer> heap5 = new MyHeap<>();
        PrgState state5 = new PrgState(stk5, symtab5, out5, st5, fileT5,heap5,3);
        IRepo repo5 = null;
        try{
            repo5 = new Repository("D:\\ubb\\MAP\\lab2-modif2\\src\\fileState5.txt");
        }catch (IOException e)
        {
            System.out.println(e.toString());
        }
        Ctrl cont5=new Ctrl(repo5);
        */

        MyIDictionary<String, Integer> symtab5 = new MyDictionary<String, Integer>();
        MyIStack<IStmt> stk5 = new MyStack<IStmt>();
        MyIList<Integer> out5 = new MyList<Integer>();
        IFileTable<Tuple> fileT5 = new FileTable<Tuple>();
        ILockTable lock= new LockTable();
        ILatch<Integer,Integer> la=new Latch<>();
        /*IStmt firstLine = new CompStmt(new NewStmt("v1", new ConstExp(20)),
                new CompStmt(new NewStmt("v2", new ConstExp(30)),
                        new newLock("x")));
        IStmt lastLine = new CompStmt(new AssignStmt("z", new ConstExp(400)),
                new CompStmt(new lockStatement("x"), new CompStmt(
                        new PrintStmt(new rH("v1")), new CompStmt(
                        new unlock("x"), new CompStmt(new lockStatement("q"),
                        new CompStmt(new PrintStmt(new rH("v2")),new unlock("q")))
                ))));

        IStmt fork1 = new ForkStatement(new CompStmt(new lockStatement("x"), new CompStmt(
                new wH("v1", new ArithExp(2,new rH("v1"), new ConstExp(1))),
                new CompStmt(new unlock("x"), new CompStmt(new lockStatement("x"),
                        new CompStmt(new wH("v1", new ArithExp(1,new rH("v1"),
                                new ConstExp(1))), new unlock("x")))))));

        IStmt fork2 = new ForkStatement(new CompStmt(new lockStatement("q"),
                new CompStmt(new wH("v2", new ArithExp(1,new rH("v2"), new ConstExp(5))),
                        new CompStmt(new unlock("q"),
                                new CompStmt(new unlock("q"),
                                        new CompStmt(new AssignStmt("m", new ConstExp(100)),
                                                new CompStmt(new lockStatement("q"),
                                                        new CompStmt(new wH("v2", new ArithExp(1,new rH("v2"),
                                                                new ConstExp(1))),new unlock("q")))))))));

        IStmt st5 = new CompStmt(firstLine, new CompStmt(fork1, new CompStmt(new newLock("q"), new CompStmt(fork2, lastLine))));
        */
        IStmt f1=new CompStmt(new wH("v1",new ArithExp(3,new rH("v1"),new ConstExp(10))),new CompStmt
                (new PrintStmt(new rH("v1")),new CountDownStmt("cnt")));
        IStmt f2=new CompStmt(new wH("v2",new ArithExp(3,new rH("v2"),new ConstExp(10))),new CompStmt
                (new PrintStmt(new rH("v2")),new CountDownStmt("cnt")));
        IStmt f3=new CompStmt(new wH("v3",new ArithExp(3,new rH("v3"),new ConstExp(10))),new CompStmt
                (new PrintStmt(new rH("v3")),new CountDownStmt("cnt")));
        IStmt s5= new CompStmt(new NewStmt("v1",new ConstExp(2)),new CompStmt(new NewStmt("v2" ,
                new ConstExp(3)),new CompStmt(new NewStmt("v3",new ConstExp(4)),
                new CompStmt(new NewLatchStmt("cnt",new rH("v2")),new CompStmt(new ForkStatement(f1),
                        new CompStmt(new ForkStatement(f2),new CompStmt(new ForkStatement(f3), new CompStmt(new AwaitStmt("cnt"),
                                new CompStmt(new PrintStmt(new VarExp("cnt")),new CompStmt(new CountDownStmt("cnt"),
                                        new PrintStmt(new VarExp("cnt"))))))))))));
        MyIHeap<Integer> heap5 = new MyHeap<>();
        PrgState state5 = new PrgState(stk5, symtab5, out5, s5, fileT5,heap5,lock,la,1);
        IRepo repo5 = null;
        try{
            repo5 = new Repository("C:\\Users\\Lexi\\Desktop\\map\\lab-all\\src\\fileState1.txt");
        }catch (IOException e)
        {
            System.out.println(e.toString());
        }
        repo5.addPrg(state5);
        Ctrl cont5=new Ctrl(repo5);
        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));

        menu.addCommand(new RunCommand("1", s5.toString(), cont5));
        menu.show();

    }
}
