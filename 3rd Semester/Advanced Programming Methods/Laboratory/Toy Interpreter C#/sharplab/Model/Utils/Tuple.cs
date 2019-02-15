using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace sharplab.Model.Utils
{
    class Tuple
    {
        private string name;
        private StreamReader s;

        public Tuple(string name, StreamReader s)
        {
            this.s = s;
            this.name = name;
        }

        public string GetName()
        {
            return this.name;
        }

        public StreamReader GetStream()
        {
            return this.s;
        }
    }
}
