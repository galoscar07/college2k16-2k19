using sharplab.Controller;
using sharplab.Model.Expressions;
using sharplab.Model.Statements;
using sharplab.Model.Utils;
using sharplab.Repo;
using sharplab.View;
using sharplab.View.Commands;
using System;

namespace sharplab
{
    class Program
    {
        static void Main(string[] args)
        {

            IMyDictionary<string, int> symtab = new MyDictionary<string, int>();
            IMyStack<IStmt> stk = new MyStack<IStmt>();
            IMyList<int> o = new MyList<int>();
            IFileTable<Model.Utils.Tuple> fileT = new FileTable<Model.Utils.Tuple>();
            IStmt st1 = new CompStmt(new AssignStmt("v", new ConstExp(2)), new PrintStmt(new VarExp("v")));
            PrgState state = new PrgState(stk, symtab, o, st1, fileT);
            IRepo repo = new Repository(state, "fileState1.txt");
            Ctrl cont = new Ctrl(repo);


            IMyDictionary<string, int> symtab2 = new MyDictionary<string, int>();
            IMyStack<IStmt> stk2 = new MyStack<IStmt>();
            IMyList<int> o2 = new MyList<int>();
            IFileTable<Model.Utils.Tuple> fileT2 = new FileTable<Model.Utils.Tuple>();
            IStmt st2 = new CompStmt(new OpenRFileStmt("f", "/Users/oscar/Documents/College/3rd Semester/Advanced Programming Methods/Laboratory/C#LabAssignment/sharplab/View/file1.txt"),
                        new CompStmt(new ReadFileStmt(new VarExp
                        ("f"), "g"), new CompStmt(new PrintStmt(new VarExp("g")), new CloseRFileStmt(new VarExp("f")))));
            PrgState state2 = new PrgState(stk2, symtab2, o2, st2, fileT2);
            IRepo repo2 = new Repository(state2, "fileState2.txt");
            Ctrl cont2 = new Ctrl(repo2);


            IMyDictionary<string, int> symtab3 = new MyDictionary<string, int>();
            IMyStack<IStmt> stk3 = new MyStack<IStmt>();
            IMyList<int> o3 = new MyList<int>();
            IFileTable<Model.Utils.Tuple> fileT3 = new FileTable<Model.Utils.Tuple>();
            IStmt st3 = new CompStmt(new AssignStmt("a", new ArithExp("-", new ConstExp(2), new ConstExp(2))), new
                        CompStmt(new IfStmt(new VarExp("a"), new AssignStmt("v", new ConstExp(2)), new AssignStmt("v",
                        new ConstExp(4))), new PrintStmt(new VarExp("v"))));
            PrgState state3 = new PrgState(stk3, symtab3, o3, st3, fileT3);
            IRepo repo3 = new Repository(state3, "fileState3.txt");
            Ctrl cont3 = new Ctrl(repo3);

            TextMenu menu = new TextMenu();
            menu.AddCommand(new ExitCommand("0", "exit"));
            menu.AddCommand(new RunCommand("1", st1.ToString(), cont));
            menu.AddCommand(new RunCommand("2", st2.ToString(), cont2));
            menu.AddCommand(new RunCommand("3", st3.ToString(), cont3));
            menu.Show();
        }
    }
}
