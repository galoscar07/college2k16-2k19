package Repo;

import Model.PrgState;

import java.io.IOException;
import java.util.List;

public interface IRepo {
    void logPrgStateExec(PrgState state);
    void CloseFile();
    List<PrgState> getPrgList();
    void setPrgList(List<PrgState> st);
    void addPrg(PrgState p);
    void serializePrgState(PrgState myState) throws IOException;
    PrgState deserializePrgState() throws IOException, ClassNotFoundException;
}
