package Model.Utils;

import Exceptions.MyDictionaryException;

import java.util.Map;

public interface MyIHeap<V> {
    String toString();
    V get(Integer key);
    void alloc(V value);
    Integer getCurr();
    void update(Integer key, V value);
    Map<Integer,V> getContent();
    void setHeap(Map<Integer,Integer> heap);
    void print();
}
