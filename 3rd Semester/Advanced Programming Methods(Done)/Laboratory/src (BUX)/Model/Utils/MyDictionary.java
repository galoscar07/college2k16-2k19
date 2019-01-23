package Model.Utils;
import Exceptions.MyDictionaryException;

import java.util.*;

public class MyDictionary<K,V> implements MyIDictionary<K,V>{

    private Map<K,V> map;
    public MyDictionary()
    {
        map=new HashMap<K,V>();
    }

    public Map<K, V> getMap() {
        return map;
    }

    public void setMap(Map<K, V> map) {
        this.map = map;
    }

    public void put(K key, V val){
        map.put(key,val);
    }

    public String toString(){
        String msg = "";
        for(K name:map.keySet())
        {
            String key = name.toString();
            msg += key + "-->" + map.get(key).toString()+";";
        }
        return msg;
    }
    public V lookup(K key) throws MyDictionaryException{
        if(map.get(key)!=null)
            return map.get(key);
        else
            throw new MyDictionaryException("Nonexistent value!");
    }

    public int isDefined(K key){
        if (map.get(key)!=null)
            return 1;
        return 0;
    }

    public void update(K key, V val){
        map.put(key,val);
    }

    public void print() {

        for(K name:map.keySet()) {
            String key = name.toString();
            System.out.println(key + " " + map.get(key));
        }

    }

    public Map<K,V> getContent(){return map;}
}

