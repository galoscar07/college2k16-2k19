package view;

import controller.Controller;
import model.ProgramState;
import model.Tuple;
import model.containers.*;
import model.expressions.*;
import model.statements.*;
import repository.IProgramStateRepository;
import repository.ProgramStateRepository;


import java.io.BufferedReader;

class Interpreter {
    public static void main(String[] args) {
        Statement s1 = new AssignStatement("v", new ConstExpression(10));
        Statement s2 = new CompoundStatement(new AssignStatement("v", new ArithmeticExpression(new VariableExpression("v"), '-', new ConstExpression(1))), new PrintStatement(new VariableExpression("v")));
        Statement s3 = new WhileStatement(new BooleanExpression(new VariableExpression("v"),"!=",new ConstExpression(0)), s2);
        Statement ex1 = new CompoundStatement(s1, s3);
        IExecStack<Statement> es1 = new ExecStack<>();
        es1.push(ex1);
        IDictionary<String, Integer> dict1 = new Dictionary<>();
        IList<Integer> list1 = new MyList<>();
        IDictionary<Integer, Tuple<String, BufferedReader>> ft1 = new Dictionary<>();
        IHeap<Integer, Integer> h1 = new Heap<>();
        ProgramState prg1 = new ProgramState(1, es1, dict1, list1, ft1, h1);
        IProgramStateRepository repo1 = new ProgramStateRepository("output/log1.txt");
        repo1.addProgramState(prg1);
        Controller ctr1 = new Controller(repo1);

        Statement a1 = new CompoundStatement(new OpenFileStatement("f1", "test1.in"),new OpenFileStatement("f2","test2.in"));
        Statement a2 = new CompoundStatement(new ReadFileStatement(new VariableExpression("f1"),"a"), new PrintStatement(new VariableExpression("a")));
        Statement a3 = new CloseFileStatement(new VariableExpression("f1"));
        Statement ex2 = new CompoundStatement(new CompoundStatement(a1, a2),a3);
        IExecStack<Statement> es2 = new ExecStack<>();
        es2.push(ex2);
        IDictionary<String, Integer> dict2 = new Dictionary<>();
        IList<Integer> list2 = new MyList<>();
        IDictionary<Integer, Tuple<String, BufferedReader>> ft2 = new Dictionary<>();
        IHeap<Integer, Integer> h2 = new Heap<>();
        ProgramState prg2 = new ProgramState(1, es2, dict2, list2, ft2, h2);
        IProgramStateRepository repo2 = new ProgramStateRepository("output/log2.txt");
        repo2.addProgramState(prg2);
        Controller ctr12 = new Controller(repo2);

        Statement ex3 = new CompoundStatement(
                new AssignStatement("v", new ConstExpression(10)),
                new CompoundStatement(
                        new HeapAllocStatement("v", new ConstExpression(20)),
                        new CompoundStatement(
                                new HeapAllocStatement("a", new ConstExpression(22)),
                                new CompoundStatement(
                                        new AssignStatement("a", new ConstExpression(0)),
                                        new CompoundStatement(
                                                new PrintStatement(new VariableExpression("a")),
                                                new CompoundStatement(
                                                        new PrintStatement(new HeapReadingExpression("a")),
                                                        new HeapWritingStatement("a", new ConstExpression(30))
                                                )
                                        )
                                )
                        )
                )
        );
        IExecStack<Statement> es3 = new ExecStack<>();
        es3.push(ex3);
        IDictionary<String, Integer> dict3 = new Dictionary<>();
        IList<Integer> list3 = new MyList<>();
        IDictionary<Integer, Tuple<String, BufferedReader>> ft3 = new Dictionary<>();
        IHeap<Integer, Integer> h3 = new Heap<>();
        ProgramState prg3 = new ProgramState(1, es3, dict3, list3, ft3, h3);
        IProgramStateRepository repo3 = new ProgramStateRepository("output/log1.txt");
        repo3.addProgramState(prg3);
        Controller ctr3 = new Controller(repo3);



        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));
        menu.addCommand(new RunExampleCommand("1", ex1.toString(), ctr1));
        menu.addCommand(new RunExampleCommand("2", ex2.toString(), ctr12));
        menu.addCommand(new RunExampleCommand("3", ex3.toString(), ctr3));
        menu.show();
    }
}

