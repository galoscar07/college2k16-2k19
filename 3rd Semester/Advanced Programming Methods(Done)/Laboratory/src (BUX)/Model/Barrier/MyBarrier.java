package Model.Statements.Barrier;

import Model.Collections.MyDictionary;
import Model.Collections.MyIDictionary;
import Model.Collections.MyIList;
import Model.Collections.Tuple;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class MyBarrier implements MyIBarrier {
    Map<Integer, Tuple<MyIList<Integer>, Integer>> dictionary = new HashMap<Integer, Tuple<MyIList<Integer>, Integer>>();

    public Tuple<MyIList<Integer>, Integer> lookup(Integer id){
        return this.dictionary.get(id);
    }



    public boolean isDefined(Integer id){
        return this.dictionary.containsKey(id);
    }

    public void update(Integer id, Tuple<MyIList<Integer>, Integer> val){
        this.dictionary.replace(id, val);
    }

    public void add(Integer id, Tuple<MyIList<Integer>, Integer> val){
        this.dictionary.put(id, val);
    }

    public String toString(){
        String str = "\n";
        for(Integer key:dictionary.keySet()){
            str = str + key.toString();
            str = str + "->";
            Tuple<MyIList<Integer>, Integer> value = lookup(key);
            str = str + value.toString()+"\n";
        }
        return str;
    }

    public Map<Integer, Tuple<MyIList<Integer>, Integer>> getContent(){
        return this.dictionary;
    }

    public void setContent(Map<Integer, Tuple<MyIList<Integer>, Integer>> myMap){
        this.dictionary = myMap;
    }

    public void remove(Integer key) {
        this.dictionary.remove(key);
    }

    public Tuple<MyIList<Integer>, Integer> getValue(Integer key){
        return this.dictionary.get(key);
    }

    public Set<Integer> getKeys() {
        return this.dictionary.keySet();
    }

    public MyIDictionary<Integer, Tuple<MyIList<Integer>, Integer>> clone() {
        MyIDictionary<Integer, Tuple<MyIList<Integer>, Integer>> dict = new MyDictionary<Integer, Tuple<MyIList<Integer>, Integer>>();
        for(Integer key : dictionary.keySet())
            dict.add(key, dictionary.get(key));
        return dict;
    }
}
