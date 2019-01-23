using sharplab.Model.Expressions;
using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Statements
{
    class IfStmt : IStmt
    {
        Exp exp;
        IStmt thenS;
        IStmt elseS;
        public IfStmt(Exp e, IStmt t, IStmt el) { this.exp = e; this.thenS = t; this.elseS = el; }
        public override string ToString()
        {
            return "IF(" + exp.ToString() + ") THEN(" + thenS.ToString()
                    + ")ELSE(" + elseS.ToString() + ")";
        }
        public PrgState Execute(PrgState state)
        {
            IMyStack<IStmt> stk=state.GetStk();
            IMyDictionary<string, int> symTbl = state.GetSymTable();
            try
            {
                if (exp.Eval(symTbl) > 0)
                    stk.Push(thenS);
                else
                    stk.Push(elseS);
                return state;
            }
            catch
            {
                throw new Exception("Invalid expression!");
            }
        }
    }
}
