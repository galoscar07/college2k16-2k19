package repository;

import model.ProgramState;
import model.Tuple;
import model.exceptions.RepositoryException;
import model.statements.Statement;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map.Entry;

public class ProgramStateRepository implements IProgramStateRepository {
    private List<ProgramState> programStates=new ArrayList<>();
    private String logFilePath;

    public ProgramStateRepository(ProgramState p,String logPath) {
        programStates.add(p);
        logFilePath = logPath;
    }

    public ProgramStateRepository(String logPath) {
        logFilePath = logPath;
    }

    @Override
    public void addProgramState(ProgramState ps) {
        programStates.add(ps);
    }

    @Override
    public List<ProgramState> getProgramList() {
        return programStates;
    }

    @Override
    public void setProgramList(List<ProgramState> list) {
        programStates = list;
    }

    @Override
    public void logProgramStateExec(ProgramState p) {
        PrintWriter logFile;
        try {
            logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        } catch (IOException e) {
            throw new RepositoryException("Failed to create log file.");
        }

        logFile.println("ExeStack:");
        for (Statement e : p.getExecStack().toArrayList()) {
            logFile.println(e);
        }

        logFile.println("SymTable:");
        for (Entry<String, Integer> e : p.getSymbolTable().toArrayList()) {
            logFile.println(e.getKey() + " --> " + e.getValue());
        }

        logFile.println("Out:");
        for (Integer e : p.getList().toArrayList()) {
            logFile.println(e);
        }

        logFile.println("FileTable:");
        for (Entry<Integer, Tuple<String, BufferedReader>> e : p.getFileTable().toArrayList()) {
            logFile.println(e.getKey() + "-->" + e.getValue().x);
        }

        logFile.println("Heap:");
        for (Entry<Integer, Integer> e : p.getHeap().toArrayList()) {
            logFile.println(e.getKey() + "-->" + e.getValue());
        }

        logFile.close();
    }

}
