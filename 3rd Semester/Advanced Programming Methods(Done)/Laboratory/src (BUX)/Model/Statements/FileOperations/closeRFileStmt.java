package Model.Statements.FileOperations;

import Model.*;
import Model.Expressions.Exp;
import Exceptions.MyControllerException;
import Exceptions.MyStmtException;
import Model.Statements.IStmt;
import Model.Utils.IFileTable;
import Model.Utils.MyIDictionary;
import Model.Utils.MyIHeap;
import Model.Utils.Tuple;

import java.io.BufferedReader;
import java.io.IOException;

public class closeRFileStmt implements IStmt
{
    private Exp exp;

    public closeRFileStmt(Exp exp)
    {
        this.exp = exp;
    }
   public PrgState execute(PrgState state) throws MyControllerException {
        MyIDictionary<String, Integer> dict = state.getSymTable();
       MyIHeap<Integer> heap=state.getHeap();
        IFileTable<Tuple> tpl = state.getFT();

        try{
            int val = exp.eval(dict,heap);
            Tuple tup = tpl.get(val);
            if(tup != null)
            {
                BufferedReader bf = tup.getBf();
                bf.close();
                tpl.remove(val);
            }
            else
                throw new MyControllerException("The file does not exist!");
        }catch (MyStmtException e)
        {
            throw new MyControllerException(e);
        }catch (IOException e)
        {
            e.printStackTrace();
        }
        return null;
    }

    public String toString() {
        return "Closing file";
    }
}
