package Model.Expressions;

import Exceptions.MyDictionaryException;
import Exceptions.MyStmtException;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;

public class rH extends Exp {
    private String Id;

    public rH(String Id){this.Id=Id;}


    public int eval(MyIDictionary<String, Integer> tbl, MyIHeap<Integer> hp) throws MyStmtException {
        try{
            int adr=tbl.lookup(Id);
            return hp.get(adr);
        }
        catch(MyDictionaryException e){
            throw new MyStmtException(e);
        }
    }

    public String toString() {
        return "rH("+Id+")";
    }
}
