package Model.Expressions;

import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;

public class ConstExp extends Exp{
    private int number;
    public ConstExp(int number){this.number=number;}
    public int eval(MyIDictionary<String,Integer> tbl, MyIHeap<Integer> hp) {return number;}
    public String toString(){return ""+number;}
}
