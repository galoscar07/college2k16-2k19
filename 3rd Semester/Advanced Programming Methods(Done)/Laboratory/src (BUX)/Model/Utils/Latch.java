package Model.Utils;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Latch<V> implements ILatch<Integer, V> {

    private HashMap<Integer, V> latchTable;
    private int nextFree;

    public Latch(){
        latchTable = new HashMap<>();
        nextFree = 1;
    }

    @Override
    public synchronized Integer add(V val) {
        latchTable.put(nextFree, val);
        return nextFree++;
    }

    @Override
    public synchronized V get(Integer key) throws Exception {
        if(latchTable.get(key) == null)
            throw new Exception("Index out of bound!");

        return latchTable.get(key);
    }

    @Override
    public boolean containsKey(Integer key) {
        return latchTable.get(key) != null;
    }

    @Override
    public synchronized void update(Integer key, V value) throws Exception {
        if(latchTable.get(key) == null)
            throw new Exception("Index out of bound!");

        latchTable.put(key, value);
    }

    @Override
    public String toString() {
        String msg = "";
        for(Integer elem : latchTable.keySet())
        {
            msg = latchTable.toString() + " -> " + latchTable.get(elem) + '\n' + msg;
        }

        return msg;
    }
}

