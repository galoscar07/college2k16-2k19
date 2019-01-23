package Model.Utils;

import java.util.HashMap;
import java.util.Map;

public class FileTable<T> implements IFileTable<T>
{
    private Map<Integer, T> fileT;
    private int idx;

    public FileTable()
    {
        this.fileT = new HashMap<>();
        this.idx = 0;
    }

    public void add(T elem) {
        idx++;
        fileT.put(idx, elem);
    }

    public int getKey() {return idx;}

    public T get(int i) {return fileT.get(i);}

    public void remove(int key) {fileT.remove(key);}

    public String toString() {
        String msg = "";
        for(int i:fileT.keySet())
        {
            Tuple tup = (Tuple)fileT.get(i);
            msg += i+" " + tup.getName() + '\n';
        }
        return msg;
    }

    public HashMap<Integer, T> getFT(){return (HashMap<Integer, T>) fileT; }
}
