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

public class readFileStatement implements IStmt
{
    private Exp exp;
    private String name;

    public readFileStatement(Exp exp, String name)
    {
        this.exp = exp;
        this.name = name;
    }

    public PrgState execute(PrgState state) throws MyControllerException {
        MyIDictionary<String, Integer> symtab = state.getSymTable();
        IFileTable<Tuple> tpl = state.getFT();
        MyIHeap<Integer> heap=state.getHeap();

        try{
            int val = exp.eval(symtab,heap);
            Tuple tup = tpl.get(val);

            if(tup != null)
            {
                BufferedReader bf = tup.getBf();
                String st = bf.readLine();
                if(st != null)
                    if(symtab.isDefined(name)==0)
                        symtab.put(name, Integer.parseInt(st));
                    else
                        symtab.put(name, Integer.parseInt(st));
                else
                    symtab.put(name, 0);
            }
            else
                throw new MyControllerException("File does not exist!");
        }
        catch (MyStmtException e)
        {
            throw new MyControllerException(e);
        }catch (IOException e)
        {
            System.out.println(e.toString());
        }
        return null;
    }

    public String toString() {
        return "Reading from: " + this.exp.toString();
    }
}
