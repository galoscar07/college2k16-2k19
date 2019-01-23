package Model.Utils;

public interface ILockTable {
    int add(int el);
    int get(int key) throws Exception;
    boolean isKey(int key);
    void update(int key, int val);
}
