using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Utils
{
    interface IMyStack<T>
    {
        void Push(T el);
        T Pop();
        void IsEmpty();
        Stack<T> GetStk();

    }
}
