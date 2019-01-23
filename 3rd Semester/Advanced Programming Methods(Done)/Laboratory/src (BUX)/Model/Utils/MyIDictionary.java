package Model.Utils;

import Exceptions.MyDictionaryException;

import java.util.Map;

public interface MyIDictionary<K,V> {
    Map<K,V> getContent();
    void put(K key,V value);
    String toString();
    V lookup(K key) throws MyDictionaryException;
    int isDefined(K key);
    void update(K key,V val);
    void setMap(Map<K, V> map);
}
