package domain.exp;

import domain.adt.MyIHeap;
import domain.adt.MyIDictionary;
import exception.DivideByZeroException;
import exception.UnknownComparisonExpression;
import exception.UnknownVariableException;

public class NotExp extends Exp{
    private Exp exp;
    public NotExp(Exp exp){
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
        } catch (UnknownVariableException e) {
            e.printStackTrace();
        } catch (DivideByZeroException e) {
            e.printStackTrace();
        } catch (UnknownComparisonExpression e) {
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
