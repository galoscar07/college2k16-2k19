package Model.Utils;

import java.util.List;

public interface MyIList<E>{
    void add(E el);
    String toString();
    void print();
    List<E> getContent();
}
