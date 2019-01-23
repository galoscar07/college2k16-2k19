package repository;

import model.ProgramState;

import java.util.List;

public interface IProgramStateRepository {
    void addProgramState(ProgramState ps);

    void logProgramStateExec(ProgramState st);

    List<ProgramState> getProgramList();

    void setProgramList(List<ProgramState> states);
}
