using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Utils
{
    interface IFileTable<T>
    {
        void Add(Tuple elem);
        int GetKey();
        Tuple Get(int i);
        void Remove(int key);
        IDictionary<int,Tuple> GetFT();
    }
}
