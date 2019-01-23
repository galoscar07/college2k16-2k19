package model.containers;

import java.util.ArrayList;

public interface IList<T> {
    void add(T el);
    T get(int index);
    ArrayList<T> toArrayList();
}
