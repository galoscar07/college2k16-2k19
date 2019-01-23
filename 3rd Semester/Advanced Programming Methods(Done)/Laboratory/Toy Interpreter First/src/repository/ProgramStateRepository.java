package repository;

import model.ProgramState;
import model.Tuple;
import model.exceptions.RepositoryException;
import model.statements.Statement;

import java.io.*;
import java.util.ArrayList;
import java.util.Map.Entry;

public class ProgramStateRepository implements IProgramStateRepository {
    private ArrayList<ProgramState> programStates;
    private String logFilePath;

    public ProgramStateRepository(String logPath) {
        programStates = new ArrayList<>();
        logFilePath = logPath;
    }

    @Override
    public void addProgramState(ProgramState ps) {
        programStates.add(ps);
    }

    @Override
    public ProgramState getCurrentProgram() {
        return programStates.get(0);
    }

    @Override
    public void logProgramStateExec() {
        PrintWriter logFile;
        try {
            logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        } catch (IOException e) {
            throw new RepositoryException("Failed to create log file.");
        }

        logFile.println("ExeStack:");
        for (Statement e : this.getCurrentProgram().getExecStack().toArrayList()) {
            logFile.println(e);
        }

        logFile.println("SymTable:");
        for (Entry<String, Integer> e : this.getCurrentProgram().getSymbolTable().toArrayList()) {
            logFile.println(e.getKey() + " --> " + e.getValue());
        }

        logFile.println("Out:");
        for (Integer e : this.getCurrentProgram().getList().toArrayList()) {
            logFile.println(e);
        }

        logFile.println("FileTable:");
        for (Entry<Integer, Tuple<String, BufferedReader>> e : this.getCurrentProgram().getFileTable().toArrayList()) {
            logFile.println(e.getKey() + "-->" + e.getValue().x);
        }

        logFile.println("Heap:");
        for (Entry<Integer, Integer> e : this.getCurrentProgram().getHeap().toArrayList()) {
            logFile.println(e.getKey() + "-->" + e.getValue());
        }

        logFile.close();
    }

}
