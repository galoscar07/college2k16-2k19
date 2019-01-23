package Model.Utils;

import java.util.HashMap;

public interface IFileTable<T>
{
    public void add(T elem);
    public int getKey();
    public T get(int i);
    public void remove(int key);
    public HashMap<Integer,T> getFT();
}
