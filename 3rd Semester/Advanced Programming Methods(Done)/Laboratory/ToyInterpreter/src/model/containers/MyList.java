package model.containers;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements IList<T> {
    private List<T> list = new ArrayList<>();

    @Override
    public void add(T el) {
        list.add(el);
    }

    @Override
    public T get(int index) {
        return list.get(index);
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        for (T e : list) {
            s.append(e);
            s.append('\n');
        }
        return s.toString();
    }

    @Override
    public ArrayList<T> toArrayList() {
        ArrayList<T> l = new ArrayList<>();
        l.addAll(list);
        return l;
    }
}
