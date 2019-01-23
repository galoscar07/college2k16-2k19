using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.View.Commands
{
    abstract class Command
    {
        private string name, desc;

        public Command(string name, string description)
        {
            this.name = name;
            this.desc = description;
        }

        public abstract void Execute();

        public string GetName()
        {
            return this.name;
        }

        public string GetDescription()
        {
            return this.desc;
        }

        public override string ToString()
        {
            return this.name + ": " + this.desc;
        }

    }
}
