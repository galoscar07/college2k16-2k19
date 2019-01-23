package model.containers;

import model.exceptions.ExecStackException;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;

public class ExecStack<T> implements IExecStack<T> {

    private Deque<T> stack;

    public ExecStack() {
        stack = new ArrayDeque<>();
    }

    @Override
    public void push(T e) {
        stack.push(e);
    }

    @Override
    public T pop() {
        if (stack.isEmpty())
            throw new ExecStackException("The stack is empty.");
        return stack.pop();
    }

    @Override
    public boolean isEmpty() {
        return stack.size() == 0;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (T a : stack) {
            sb.append(a);
            sb.append('\n');
        }
        return sb.toString();
    }

    @Override
    public ArrayList<T> toArrayList() {
        ArrayList<T> l = new ArrayList<>();
        l.addAll(stack);
        return l;
    }
}
