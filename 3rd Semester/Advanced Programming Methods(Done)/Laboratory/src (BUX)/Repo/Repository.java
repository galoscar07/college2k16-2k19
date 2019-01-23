package Repo;
import Model.*;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Repository implements IRepo {
    private List<PrgState> states;
    private PrintWriter filewrt;

    public Repository(String logFilePath) throws IOException {
        states = new ArrayList<>();
        try {
            filewrt = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void addPrg(PrgState p){
        states.add(p);
    }

    public void logPrgStateExec(PrgState state) {
        filewrt.print("Program State #");
        filewrt.println(state.getId());
        filewrt.println("***Execution Stack***\n");
        filewrt.println(state.getStk().toString());
        filewrt.println("***Symbol Table***\n");
        filewrt.println(state.getSymTable().toString());
        filewrt.println("***Out***\n");
        filewrt.println(state.getOut().toString());
        filewrt.println("***File Table***\n");
        filewrt.println(state.getFT().toString());
        filewrt.println("***Heap***\n");
        filewrt.println(state.getHeap().toString());
        filewrt.println("***Lock Table***\n");
        filewrt.println(state.getLockTable().toString());
        filewrt.println("--------------------------------------------------------");
    }

    public void CloseFile() {
        filewrt.close();
    }

    public List<PrgState> getPrgList() {
        return states;
    }
    public void setPrgList(List<PrgState> st) {
        this.states=st;
    }


    @Override
    public void serializePrgState(PrgState myState) throws IOException {
        FileOutputStream myFile = new FileOutputStream("prgState.ser");
        ObjectOutputStream outStream = new ObjectOutputStream(myFile);
        outStream.writeObject(myState);
        outStream.close();
    }

    @Override
    public PrgState deserializePrgState() throws IOException, ClassNotFoundException {
        FileInputStream myFile = new FileInputStream("prgState.ser");
        ObjectInputStream inStream = new ObjectInputStream(myFile);
        PrgState myState = (PrgState) inStream.readObject();
        inStream.close();
        return myState;
    }
}

