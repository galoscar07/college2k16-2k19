package Model.Utils;
import java.util.*;

public class MyList<E> implements MyIList<E>{
    private List<E> list;
    public MyList() {
        list = new ArrayList<E>();
    }
    public void add(E el){
        list.add(el);
    }

    public String toString(){
        String msg="";
        for (E el:list)
            msg+=el.toString()+";";
        return msg;
    }

    public List<E> getContent(){return list;}

    public void print() {
        for(E l:list)
        {
            String str = l.toString();
            System.out.println(str);
        }
    }

}