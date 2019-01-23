package Model.Statements.FileOperations;

import Model.Statements.IStmt;
import Model.Utils.MyIDictionary;
import Model.Utils.IFileTable;
import Model.PrgState;
import Exceptions.MyControllerException;
import Model.Utils.Tuple;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class openRFileStmt implements IStmt
{
    private String varName;
    private String filename;

    public openRFileStmt(String varName, String filename )
    {
        this.varName = varName;
        this.filename = filename;
    }

    public PrgState execute(PrgState state) throws MyControllerException {
        MyIDictionary<String, Integer> symtab = state.getSymTable();
        IFileTable<Tuple> fileT = state.getFT();

        try{
            for(int i = 1; i<=fileT.getKey();i++)
            {
                Tuple tpl = fileT.get(i);
                if(tpl != null && filename.equals(tpl.getName()))
                    throw new MyControllerException("The file already exists!");
            }
            BufferedReader bf = new BufferedReader(new FileReader(this.filename));
            Tuple tpl = new Tuple(filename, bf);
            fileT.add(tpl);
            symtab.put(this.varName, fileT.getKey());
        }catch (FileNotFoundException e)
        {
            System.out.println(e.toString());
        }
        return null;
    }
    public String toString() {
        return "Opening: " + filename;
    }
}
