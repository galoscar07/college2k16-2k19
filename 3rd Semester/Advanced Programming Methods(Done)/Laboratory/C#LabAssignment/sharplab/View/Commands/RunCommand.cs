using sharplab.Controller;
using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.View.Commands
{
    class RunCommand : Command
    {
        private Ctrl ctr;
        public RunCommand(string name, string description, Ctrl ctr) : base(name, description)
        {
            this.ctr = ctr;
        }

        public override void Execute()
        {
            ctr.AllStep();
        }
        public override string ToString()
        {
            return this.GetName() + "." + this.GetDescription() + "\n";
        }

    }
}
