package model.containers;

import java.util.ArrayList;

public interface IExecStack<T> {
    void push(T e);

    T pop();

    boolean isEmpty();

    ArrayList<T> toArrayList();
}
