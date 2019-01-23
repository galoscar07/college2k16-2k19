package model.containers;

import java.util.ArrayList;
import java.util.Map;
import java.util.Map.Entry;

public interface IHeap<K, V> {
    K put(V value);

    V get(K key);

    void update(K key, V value);

    boolean contains(K key);

    Map<K, V> getContent();

    void setContent(Map<K, V> newContent);

    ArrayList<Entry<K, V>> toArrayList();
}
