using System;
using System.Collections.Generic;
using System.Text;

namespace sharplab.Model.Utils
{
    public interface IMyDictionary<K,V>
    {
        SortedDictionary<K, V> GetDictionary();
        void Put(K key, V value);
        V LookUp(K key);
        int IsDefined(K key);
        void Update(K key, V value);
    }
}
