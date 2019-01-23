package model.containers;

import model.exceptions.DictionaryException;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Dictionary<T, E> implements IDictionary<T, E> {

    private Map<T, E> dict = new HashMap<>();

    public Dictionary(){}

    public Dictionary(Map<T,E> map){
        dict=map;
    }

    @Override
    public boolean contains(T k) {
        return dict.containsKey(k);
    }

    @Override
    public E get(T k) {
        if (!dict.containsKey(k))
            throw new DictionaryException("Key not found.");
        return dict.get(k);
    }

    @Override
    public void add(T k, E e) {
        dict.put(k, e);
    }

    @Override
    public void update(T k, E e) {
        dict.put(k, e);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<T, E> e : dict.entrySet()) {
            sb.append(e.getKey()).append(" ").append(e.getValue()).append('\n');
        }
        return sb.toString();
    }

    @Override
    public ArrayList<Entry<T, E>> toArrayList() {
        ArrayList<Entry<T, E>> l = new ArrayList<>();
        l.addAll(dict.entrySet());
        return l;
    }

    @Override
    public void remove(T k) {
        dict.remove(k);
    }

    public Map<T, E> getContent() {
        return dict;
    }

    @Override
    public void setContent(Map<T, E> d) {
        dict = d;
    }

    @Override
    public void empty() {
        dict.clear();
    }

    @Override
    public IDictionary<T, E> getCopy() {
        return new Dictionary<T,E>(new HashMap<T,E>(dict));
    }
}
