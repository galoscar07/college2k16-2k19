using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Expressions
{
    class VarExp : Exp
    {
        private string id;
        public VarExp(string id) { this.id = id; }
        public override int Eval(IMyDictionary<string,int> tbl)
        { 
            return tbl.LookUp(id);
        }
        public override string ToString() { return id; }
    }
}
