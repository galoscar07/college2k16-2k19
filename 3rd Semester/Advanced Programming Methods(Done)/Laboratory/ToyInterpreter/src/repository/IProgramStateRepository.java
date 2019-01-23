package repository;

import model.ProgramState;

import java.util.List;

public interface IProgramStateRepository {
    void addProgramState(ProgramState ps);
    List<ProgramState> getProgramList();
    void setProgramList(List<ProgramState> list);
    void logProgramStateExec(ProgramState p);
}
