using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Expressions
{
    class ArithExp : Exp
    {
        Exp e1;
        Exp e2;
        string op;

        public ArithExp(string op, Exp e1, Exp e2)
        {
            this.e1 = e1;
            this.e2 = e2;
            this.op = op;
        }
      
        public override int Eval(IMyDictionary<string, int> tbl)
        {
       
            if (op == "+")
                return e1.Eval(tbl) + e2.Eval(tbl);
            if (op == "-")
                return e1.Eval(tbl) - e2.Eval(tbl);
            if (op == "*")
                return e1.Eval(tbl) * e2.Eval(tbl);
            if (op == "/")
            {
                if (e2.Eval(tbl) == 0)
                    throw new Exception("Division by zero!!!");
                else
                    return e1.Eval(tbl) / e2.Eval(tbl);
            }
            else
                throw new Exception("The operand does not exist!!");
        }


        public override string ToString()
        {
            return "(" + e1 + op + e2 + ")";
        }
    }
}
