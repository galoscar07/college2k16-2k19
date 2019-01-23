package Model.Utils;

import Exceptions.MyDictionaryException;

import java.util.HashMap;
import java.util.Map;

public class MyHeap<V> implements MyIHeap<V> {
    private Integer curr;
    private Map<Integer,V> map;
    public MyHeap()
    {
        map=new HashMap<>();
        curr= new Integer(1);
    }

    public MyHeap(MyIHeap<Integer> heap) {
        this.map= (Map<Integer, V>) heap;
    }


    public String toString(){
        String msg = "";
        for(Integer name:map.keySet())

            msg += name + "-->" + map.get(name).toString()+";";
        return msg;
    }
    public V get(Integer key) {
        return map.get(key);

    }

    public void print() {

        for(Integer name:map.keySet()) {
            String key = name.toString();
            System.out.println(key + "new("+key+"," + map.get(key)+")");
        }

    }

    public void alloc(V value){
        map.put(curr,value);
        this.curr+=1;
    }

    public Integer getCurr() {
        return this.curr;
    }

    public void update(Integer key, V value) {
        map.replace(key,value);
    }

    public void setHeap(Map<Integer,Integer> heap){this.map= (Map<Integer, V>) heap;}

    public Map<Integer,V> getContent(){return map;}
}