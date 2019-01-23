package model.containers;

import java.util.ArrayList;
import java.util.Map;
import java.util.Map.Entry;

public interface IDictionary<T, E> {
    boolean contains(T k);
    E get(T k);
    void add(T k, E e);
    void update(T k, E e);
    void remove(T k);
    ArrayList<Entry<T, E>> toArrayList();
    Map<T, E> getContent();
    void setContent(Map<T,E> d);
    IDictionary<T, E> getCopy();
    void empty();
}
