package model.statements;

import model.ProgramState;
import model.Tuple;
import model.containers.IDictionary;
import model.containers.IHeap;
import model.exceptions.FileException;
import model.expressions.Expression;

import java.io.BufferedReader;
import java.io.IOException;

public class CloseFileStatement implements Statement {
    private Expression exp;

    public CloseFileStatement(Expression e) {
        exp = e;
    }

    @Override
    public ProgramState execute(ProgramState ps) {
        //check if file is in fileTable
        IDictionary<String, Integer> st = ps.getSymbolTable();
        IHeap<Integer, Integer> h = ps.getHeap();
        Integer e = exp.eval(st, h);
        IDictionary<Integer, Tuple<String, BufferedReader>> ft = ps.getFileTable();
        if (!ft.contains(e)) {
            throw new FileException("File was not opened.");
        }

        //close the file
        BufferedReader br = ft.get(e).y;
        try {
            br.close();
        } catch (IOException e1) {
            throw new FileException("Error closing the file.");
        }

        //remove from fileTable
        ft.remove(e);
        return null;
    }

    @Override
    public String toString() {
        return "closeRFile(" + exp + ")";
    }
}
