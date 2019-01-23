package repository;

import models.ProgramState;

public interface IProgramStateRepository {
	void addProgramState(ProgramState ps);
	ProgramState getCurrentProgram(); 
}
