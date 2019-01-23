package model.containers;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Heap<V> implements IHeap<Integer, V> {
    private Map<Integer, V> map = new HashMap<>();
    private int nextFree = 1;


    @Override
    public Integer put(V value) {
        map.put(nextFree, value);
        return nextFree++;
    }

    @Override
    public Map<Integer, V> getContent() {
        return map;
    }

    @Override
    public void setContent(Map<Integer, V> newContent) {
        map = newContent;
    }


    @Override
    public void update(Integer key, V value) {
        map.put(key, value);
    }

    @Override
    public V get(Integer key) {
        return map.get(key);
    }

    @Override
    public boolean contains(Integer key) {
        return map.containsKey(key);
    }

    @Override
    public ArrayList<Entry<Integer, V>> toArrayList() {
        ArrayList<Entry<Integer, V>> l = new ArrayList<>();
        l.addAll(map.entrySet());
        return l;
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<Integer, V> e : map.entrySet()) {
            sb.append(e.getKey()).append(" ").append(e.getValue()).append('\n');
        }
        return sb.toString();
    }
}