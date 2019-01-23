package model.statements;

import model.IdGenerator;
import model.ProgramState;
import model.Tuple;
import model.containers.IDictionary;
import model.exceptions.FileException;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Map.Entry;
import java.util.Objects;

public class OpenFileStatement implements Statement {
    private String varName;
    private String filename;

    public OpenFileStatement(String v, String f) {
        varName = v;
        filename = f;
    }

    @Override
    public ProgramState execute(ProgramState ps) {
        //check if filename exists in FileTable i.e file is already open
        ArrayList<Entry<Integer, Tuple<String, BufferedReader>>> f = ps.getFileTable().toArrayList();
        for (Entry<Integer, Tuple<String, BufferedReader>> e : f) {
            if (Objects.equals(e.getValue().x, filename)) {
                throw new FileException("Filename already exists in FileTable.");
            }
        }

        //Open the file
        BufferedReader br;
        try {
            br = new BufferedReader(new FileReader(filename));
        } catch (FileNotFoundException e) {
            throw new FileException("File not found.");
        }

        //Add to FileTable and SymbolTable
        Integer id = IdGenerator.generateId();
        Tuple<String, BufferedReader> e = new Tuple<>(filename, br);
        IDictionary<Integer, Tuple<String, BufferedReader>> ft = ps.getFileTable();
        if (ft.contains(id)) {
            ft.update(id, e);
        } else {
            ft.add(id, e);
        }
        IDictionary<String, Integer> st = ps.getSymbolTable();
        if (st.contains(varName)) {
            st.update(varName, id);
        } else {
            st.add(varName, id);
        }

        return null;
    }

    @Override
    public String toString() {
        return "openRFile(" + varName + "," + filename + ")";
    }
}
