package model.statements;

import model.ProgramState;
import model.Tuple;
import model.containers.IDictionary;
import model.containers.IHeap;
import model.exceptions.FileException;
import model.expressions.Expression;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFileStatement implements Statement {
    private String varName;
    private Expression file;

    public ReadFileStatement(Expression f, String v) {
        varName = v;
        file = f;
    }

    @Override
    public ProgramState execute(ProgramState ps) {
        //check if file is in fileTable
        IDictionary<String, Integer> st = ps.getSymbolTable();
        IHeap<Integer, Integer> h = ps.getHeap();
        Integer e = file.eval(st, h);
        IDictionary<Integer, Tuple<String, BufferedReader>> ft = ps.getFileTable();
        if (!ft.contains(e)) {
            throw new FileException("File id is invalid.");
        }
        //read a line
        String line;
        try {
            line = ft.get(e).y.readLine();
        } catch (IOException exc) {
            throw new FileException("Failed to read from file.");
        }
        //parse the integer
        Integer value;
        if (line == null) {
            value = 0;
        } else {
            value = Integer.parseInt(line);
        }
        //update the symbolTable
        if (st.contains(varName)) {
            st.update(varName, value);
        } else {
            st.add(varName, value);
        }

        return null;
    }

    @Override
    public String toString() {
        return "readFile(" + file + "," + varName + ")";
    }
}
