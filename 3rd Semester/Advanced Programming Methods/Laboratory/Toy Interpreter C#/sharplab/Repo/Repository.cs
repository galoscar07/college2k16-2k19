using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace sharplab.Repo
{
    class Repository : IRepo
    {
        private int curr=0;
        private List<PrgState> states= new List<PrgState>();
        private string path;

        public Repository(PrgState state, String logFilePath)
        {
            states.Add(state);
            path=logFilePath;
        }
        public PrgState GetCrtPrg()
        {
            return states[this.curr];
        }

        public void LogPrgStateExec()
        {
            string s = "";
            s += "\n***Execution Stack***\n";
            s += states[curr].GetStk().ToString()+"\n";
            s += "***Symbol Table***\n";
            s += states[curr].GetSymTable().ToString() + "\n";
            s += "***Out***\n";
            s += states[curr].Geto().ToString() + "\n";
            s += "***File Table***\n";
            s += states[curr].GetFT().ToString() + "\n";
            s += "--------------------------------------------------------\n";
            using (StreamWriter outputFile = new StreamWriter(path, true))
            {
                outputFile.Write(s);
            }
        }

        public List<PrgState> GetPrgList()
        {
            return states;
        }
    }
    
}
