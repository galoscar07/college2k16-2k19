using sharplab.Model.Expressions;
using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Statements
{
    class AssignStmt : IStmt
    {
        string id;
        Exp exp;
        public AssignStmt(String id, Exp exp)
        {
            this.id = id;
            this.exp = exp;
        }
        public override string ToString()
        {
            return id + "=" + exp;
        }

        public PrgState Execute(PrgState state)
        {
            IMyStack<IStmt> stk=state.GetStk();
            IMyDictionary<string, int> symTbl = state.GetSymTable();
            try {
                int val = exp.Eval(symTbl);
                if (symTbl.IsDefined(id) == 1)
                    symTbl.Update(id, val);
                else
                    symTbl.Put(id, val);
                return state;
            }
            catch
            {
                throw new Exception("Invalid expression!");
            }
            
        
    }
    }
}
