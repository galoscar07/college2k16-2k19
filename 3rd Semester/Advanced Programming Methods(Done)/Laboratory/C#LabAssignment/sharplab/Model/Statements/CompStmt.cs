using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Statements
{
    class CompStmt : IStmt
    {
        IStmt first;
        IStmt snd;
        public CompStmt(IStmt first, IStmt snd)
        {
            this.first = first;
            this.snd = snd;
        }

        public override string ToString()
        {
            return first + ";" + snd;
        }

        public PrgState Execute(PrgState state)
        {
            IMyStack<IStmt> stk = state.GetStk();
            stk.Push(snd);
            stk.Push(first);
            return state;
        }
    }
}
