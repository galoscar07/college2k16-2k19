using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace sharplab.Model.Statements
{
    class OpenRFileStmt : IStmt
    {
        private String varName;
        private String filename;

        public OpenRFileStmt(string varName, string filename)
        {
            this.varName = varName;
            this.filename = filename;
        }

        public PrgState Execute(PrgState state)
        {
            IMyDictionary<string, int> symtab = state.GetSymTable();
            IFileTable<Utils.Tuple> fileT = state.GetFT();

            try
            {
                for(int i = 1; i<=fileT.GetKey();i++)
                {
                    Utils.Tuple tupl = fileT.Get(i);
                    if(tupl != null && filename.Equals(tupl.GetName()))
                        throw new Exception("The file already exists!");
            }
            StreamReader s = new StreamReader(this.filename);
            Utils.Tuple tpl = new Utils.Tuple(filename, s);
            fileT.Add(tpl);
            symtab.Put(this.varName, fileT.GetKey());
            }
            catch (FileNotFoundException e)
            {
                System.Console.WriteLine(e.ToString());
            }
            return state;
        }
        public override string ToString()
        {
            return "Opening: " + filename;
        }
    }
    
}
