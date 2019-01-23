package repository;

import model.ProgramState;

public interface IProgramStateRepository {
    void addProgramState(ProgramState ps);

    void logProgramStateExec();

    ProgramState getCurrentProgram();
}
