using sharplab.Model.Expressions;
using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace sharplab.Model.Statements
{
    class CloseRFileStmt : IStmt
    {
        private Exp exp;

        public CloseRFileStmt(Exp exp)
        {
            this.exp = exp;
        }
        public PrgState Execute(PrgState state)
        {
            IMyDictionary<string, int> dict = state.GetSymTable();
            IFileTable<Utils.Tuple> tpl = state.GetFT();

            try
            {
                int val = exp.Eval(dict);
                Utils.Tuple tup = tpl.Get(val);
                if(tup != null)
                {
                    StreamReader s = tup.GetStream();
                    s.Close();
                    tpl.Remove(val);
                }
                else
                    throw new Exception("The file does not exist!");
            }catch 
            {
                throw new Exception("Invalid expression!");
            }
            return state;
        }

        public override string ToString()
        {
            return "Closing file";
        }
    }
}
