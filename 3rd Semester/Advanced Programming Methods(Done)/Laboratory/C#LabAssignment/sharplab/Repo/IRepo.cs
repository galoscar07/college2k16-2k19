using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Repo
{
    interface IRepo
    {
        PrgState GetCrtPrg();
        void LogPrgStateExec();
        List<PrgState> GetPrgList();
    }
}
