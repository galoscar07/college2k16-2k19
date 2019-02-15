using sharplab.Model.Statements;
using sharplab.Model.Utils;
using sharplab.Repo;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Controller
{
    class Ctrl
    {
        private IRepo repo;

        public Ctrl(IRepo r) { repo = r; }


        private void OneStep(PrgState state)
        {
            IMyStack<IStmt> stk = state.GetStk();
            try
            {
                stk.IsEmpty();
            }
            catch
            {
                throw new Exception("Empty stack!\n");
            }
            IStmt crtStmt = stk.Pop();
                Console.WriteLine(crtStmt.ToString()+" ");
                crtStmt.Execute(state);

        }

        public void AllStep()
        {
            PrgState prg = repo.GetCrtPrg();
            try
            {
                while (true)
                {
                   OneStep(prg);
                   repo.LogPrgStateExec();
                   Print();
                }
            }
            catch
            {
                System.Console.WriteLine("End of program.");
            }
        }

        public void Print()
        {
            PrgState prog = repo.GetCrtPrg();
            IMyDictionary<string, int> dict = prog.GetSymTable();
            IMyList<int> list = prog.Geto();
            System.Console.WriteLine("-------------------------------------------\n");
            System.Console.WriteLine("SYM TABLE:\n"+dict.ToString() + "\n");
            System.Console.WriteLine("OUT:\n"+list.ToString() + "\n");
            System.Console.WriteLine("-------------------------------------------\n");
        }
    }
}
