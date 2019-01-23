package Model.Expressions;
import java.lang.String;

import Exceptions.MyDictionaryException;
import Exceptions.MyStmtException;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;

public class VarExp extends Exp{
    private String id;
    private int adr;
    public VarExp(String id){this.id=id;}
    public int eval(MyIDictionary<String,Integer> tbl, MyIHeap<Integer> hp) throws MyStmtException {
        try {
            adr=tbl.lookup(id);
            return adr;
        } catch (MyDictionaryException e) {
            throw new MyStmtException(e);
        }
    }
    public String toString(){return id;}
}
