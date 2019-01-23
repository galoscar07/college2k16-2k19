using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Utils
{
    class MyList<E>:IMyList<E>
    {
        private IList<E> list;
        public MyList()
        {
            list = new List<E>();
        }
        public void Add(E el)
        {
            list.Add(el);
        }

        public override string ToString()
        {
            String msg = "";
            foreach (E el in list)
                msg += el.ToString() + ";";
            return msg;
        }
    }
}
