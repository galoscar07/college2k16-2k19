package domain.adt;
import java.util.HashMap;

public class MyLockTable implements MyILockTable {

    private HashMap<Integer, Integer> lockTable;
    private int nextFree;

    public MyLockTable(){
        lockTable = new HashMap<>();
        nextFree = 0;
    }

    @Override
    public synchronized int add(int el) {
        lockTable.put(nextFree, el);
        return nextFree++;
    }

    @Override
    public synchronized int get(int key) throws Exception {
        if(lockTable.get(key) == null)
            throw new Exception("Index out of bound!");

        return lockTable.get(key);
    }

    @Override
    public synchronized boolean isKey(int key) {
        return lockTable.containsKey(key);
    }

    @Override
    public synchronized void update(int key, int val) {
        lockTable.put(key, val);
    }

    @Override
    public String toString() {
        String msg = "";
        for(int adr:lockTable.keySet())
        {
            String key = ""+adr;
            msg += key + "-->" + lockTable.get(key).toString()+";";
        }
        return msg;
    }
}


