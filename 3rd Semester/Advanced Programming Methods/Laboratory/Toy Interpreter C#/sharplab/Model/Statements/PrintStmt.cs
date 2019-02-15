using sharplab.Model.Expressions;
using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Statements
{
    class PrintStmt : IStmt
    {
        Exp exp;
        public PrintStmt(Exp exp) { this.exp = exp; }
        public override string ToString() { return "print(" + exp + ")"; }
        public PrgState Execute(PrgState state)
        {
           IMyList<int> o=state.Geto();
            IMyDictionary<string, int> symTbl = state.GetSymTable();
           try
           {
                o.Add(exp.Eval(symTbl));
                return state;
           }
           catch
           {
                throw new Exception("Invalid expression!");
           }
        }
    }
}
