package domain.adt;

import exception.MyException;

import java.util.Collection;
import java.util.Map;

public interface MyIDictionary <K, V>{
    V put(K key, V value);
    V get(K key) ;
    Collection<V> values();
    Collection<K> keys();
    V lookup(K key) throws MyException;
    V remove(K fd);
    MyIDictionary<K, V> clone();
    Map<K, V> toMap();
}
