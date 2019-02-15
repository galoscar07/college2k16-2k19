using sharplab.Model.Expressions;
using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace sharplab.Model.Statements
{
    class ReadFileStmt : IStmt
    {
        private Exp exp;
        private String name;

        public ReadFileStmt(Exp exp, String name)
        {
            this.exp = exp;
            this.name = name;
        }

        public PrgState Execute(PrgState state)
        {
            IMyDictionary<string, int> symtab = state.GetSymTable();
            IFileTable<Utils.Tuple> tpl = state.GetFT();
       
            try{
                int val = exp.Eval(symtab);
                Utils.Tuple tup = tpl.Get(val);
                if (tup != null)
                {
                    StreamReader s = tup.GetStream();
                    String st = s.ReadLine();
                    if(st != null)
                        if(symtab.IsDefined(name)==0)
                            symtab.Put(name, int.Parse(st));
                        else
                            symtab.Put(name, int.Parse(st));
                    else
                        symtab.Put(name, 0);
                }
                else
                    throw new Exception("File does not exist!");
         
            }catch (IOException e)
            {
                System.Console.WriteLine(e.ToString());
            }
            return state;
        }

        public override string ToString()
        {
            return "Reading from: " + this.exp.ToString();
        }
    }
}
