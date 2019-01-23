package Model.Utils;

import java.io.Serializable;

public interface ILatch<K, V> extends Serializable {
    K add(V val);
    V get(K key) throws Exception;
    boolean containsKey(K key);
    void update(K key, V value) throws Exception;
}

