using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Expressions
{
    class ConstExp : Exp
    {
        private int number;
        public ConstExp(int number) { this.number = number; }
        public  override int Eval(IMyDictionary<string, int> tbl) { return number; }
        public override string ToString() { return "" + number; }
    }
}
