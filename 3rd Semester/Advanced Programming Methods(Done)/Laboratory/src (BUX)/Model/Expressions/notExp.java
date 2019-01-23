package Model.Expressions;

import Exceptions.MyStmtException;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;

public class notExp extends Exp {
    private Exp exp;
    public notExp(Exp exp) {
        this.exp = exp;
    }
    @Override
    public int eval(MyIDictionary<String, Integer> symTable, MyIHeap<Integer> heap)
    {
        // if x evals to 0 => false => !false = true
        /// else !true = false
        int x = 0;
        try {
            x = this.exp.eval(symTable, heap);
        } catch (MyStmtException e) {
            e.printStackTrace();
        }
        if(x == 0)
            return 1;
        return 0;
    }

    @Override
    public String toString() {
        return "!" + this.exp.toString();
    }
}