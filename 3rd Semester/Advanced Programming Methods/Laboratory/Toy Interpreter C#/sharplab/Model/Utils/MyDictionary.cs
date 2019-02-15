using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace sharplab.Model.Utils
{
    class MyDictionary<K,V> : IMyDictionary<K,V>
    {
        private SortedDictionary<K,V> dict;

        public MyDictionary()
        {
            dict = new SortedDictionary<K,V>();
        }


        public SortedDictionary<K,V> GetDictionary()
        {
            return dict; 
        }



        public int IsDefined(K key)
        {
            if( dict.ContainsKey(key))
                return 1;
            return 0;
        }



        public V LookUp(K key)
        {
            if (this.IsDefined(key) != 0)
                return dict.GetValueOrDefault(key);
            else
                throw new Exception("Nonexistent value!");
        }



        public override string ToString()
        {
            string s = "";
            var arrayOfAllKeys = dict.Keys.ToArray();
            var arrayOfAllValues = dict.Values.ToArray();
            for (int i = 0; i < arrayOfAllKeys.Length; i++)
            {
                s += arrayOfAllKeys[i].ToString();
                s += "->";
                s += arrayOfAllValues[i].ToString();
                s += ";";
            }
            return s;
        }



        public void Put(K key, V value)
        {
            dict.Add(key, value);
        }



        public void Update(K key, V value)
        {
            dict[key] = value;
        }

    }

    
}
