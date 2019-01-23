using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.View.Commands
{
    class ExitCommand : Command
    {
        public ExitCommand(string name, string description) : base(name, description){}

        public override void Execute()
        {
            Environment.Exit(0);
        }

    }
}
