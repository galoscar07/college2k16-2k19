using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Utils
{
    class MyStack<T> : IMyStack<T>
    {
        private Stack<T> stk;
        public MyStack()
        {
            stk = new Stack<T>();
        }
        public void Push(T el)
        {
            stk.Push(el);
        }

        public override string ToString()
        {
            String msg = "";
            foreach (T el in stk)
            {
                msg += el + ";";
            }
            return msg;
        }
        public T Pop()
        {
            return stk.Pop();
        }

        public Stack<T> GetStk()
        {
            return stk;
        }

        public void IsEmpty()
        {
            if (stk.Count == 0)
                throw new Exception("Stack is empty!");
        }
    }
}
