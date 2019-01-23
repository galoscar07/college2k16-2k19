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
        Statement s = new CompoundStatement(
                new CompoundStatement(
                        new CompoundStatement(
                                new AssignStatement("v",new ConstExpression(10)),
                                new HeapAllocStatement("a",new ConstExpression(22))
                        ),
                        new ForkStatement(
                                new CompoundStatement(
                                        new HeapWritingStatement("a", new ConstExpression(30)),
                                                new CompoundStatement(
                                                        new AssignStatement("v",new ConstExpression(32)),
                                                        new CompoundStatement(
                                                        new PrintStatement(new VariableExpression("v")),
                                                    new PrintStatement(new HeapReadingExpression("a")))
                                        )
                                )
                        )
                ),
                new CompoundStatement(
                        new PrintStatement(new VariableExpression("v")),
                        new PrintStatement(new HeapReadingExpression("a"))
                ));

        /*
        v=10
        new(a,22)
        fork(
              wH(a,30)
              v=32
              Print(v)
              Print(rH(a))
            )
        Print(v)
        Print(rH(a))
        */

        Statement s2 = new CompoundStatement(
                new CompoundStatement(
                        new CompoundStatement(
                                new AssignStatement("v",new ConstExpression(10)),
                                new HeapAllocStatement("a",new ConstExpression(22))
                        ),
                        new ForkStatement(new CompoundStatement(
                                    new HeapWritingStatement("a", new ConstExpression(30)),
                                            new ForkStatement(
                                                    new CompoundStatement(
                                                            new AssignStatement("v",new ConstExpression(20)),
                                                            new PrintStatement(new VariableExpression("v"))
                                            )
                        )
                ))),
                new CompoundStatement(
                        new PrintStatement(new VariableExpression("v")),
                        new PrintStatement(new HeapReadingExpression("a"))
                ));

        /*
        v=10
        new(a,22)
        fork(
              wH(a,30)
              fork(
                    v=20
                    Print(v)
                   )
            )
        Print(v)
        Print(rH(a))
        */

        IExecStack<Statement> es1 = new ExecStack<>();
        es1.push(s);
        IDictionary<String, Integer> dict1 = new Dictionary<>();
        IList<Integer> list1 = new MyList<>();
        IDictionary<Integer, Tuple<String, BufferedReader>> ft1 = new Dictionary<>();
        IHeap<Integer, Integer> h1 = new Heap<>();
        ProgramState prg1 = new ProgramState(1, es1, dict1, list1, ft1, h1);
        IProgramStateRepository repo1 = new ProgramStateRepository("output/log1.txt");
        repo1.addProgramState(prg1);
        Controller ctr1 = new Controller(repo1);

        IExecStack<Statement> es2 = new ExecStack<>();
        es2.push(s2);
        IDictionary<String, Integer> dict2 = new Dictionary<>();
        IList<Integer> list2 = new MyList<>();
        IDictionary<Integer, Tuple<String, BufferedReader>> ft2 = new Dictionary<>();
        IHeap<Integer, Integer> h2 = new Heap<>();
        ProgramState prg2 = new ProgramState(1, es2, dict2, list2, ft2, h2);
        IProgramStateRepository repo2 = new ProgramStateRepository("output/log2.txt");
        repo2.addProgramState(prg2);
        Controller ctr12 = new Controller(repo2);

        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));
        menu.addCommand(new RunExampleCommand("1", s.toString(), ctr1));
        menu.addCommand(new RunExampleCommand("2", s2.toString(), ctr12));
        menu.show();
    }
}
