using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace sharplab.Model.Utils
{
    class FileTable<T> : IFileTable<T>
    {
        private IDictionary<int, Tuple> fileT;
        private int idx;

        public FileTable()
        {
            this.fileT = new SortedDictionary<int, Tuple>();
            this.idx = 0;
        }

        public void Add(Tuple elem)
        {
            idx++;
            fileT.Add(idx, elem);
        }

        public int GetKey() { return idx; }

        public Tuple Get(int i) { return fileT[i]; }

        public void Remove(int key) { fileT.Remove(key); }

        public override string ToString()
        {
            String msg = "";
            foreach (int i in fileT.Keys.ToArray())
            {
                Tuple tup = this.Get(i);
                msg += i + " " + tup.GetName() + '\n';
            }
            return msg;
        }

        public IDictionary<int, Tuple> GetFT() { return fileT; }
    }
}
