package model.expressions;

import model.containers.IDictionary;
import model.containers.IHeap;

public interface Expression {
    int eval(IDictionary<String, Integer> st, IHeap<Integer, Integer> heap);
}
