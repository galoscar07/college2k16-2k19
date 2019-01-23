using sharplab.Model.Utils;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Statements
{
   interface IStmt
    {
        PrgState Execute(PrgState state);
    }
}
