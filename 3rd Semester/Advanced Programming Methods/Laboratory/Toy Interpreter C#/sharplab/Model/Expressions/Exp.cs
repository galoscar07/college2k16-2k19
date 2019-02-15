using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Expressions
{
    public abstract class Exp
    {
        public abstract int Eval(IMyDictionary<string,int> tbl);
    }
}
