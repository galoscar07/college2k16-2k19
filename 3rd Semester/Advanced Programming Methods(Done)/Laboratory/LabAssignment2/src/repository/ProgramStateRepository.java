package repository;

import java.util.ArrayList;

import models.ProgramState;

public class ProgramStateRepository implements IProgramStateRepository{
	private ArrayList<ProgramState> programStates;
	
	public ProgramStateRepository() {
		programStates = new ArrayList<>();
	}
	
	
	@Override
	public void addProgramState(ProgramState ps) {
		programStates.add(ps);
	}

	@Override
	public ProgramState getCurrentProgram() {
		return programStates.get(0);
	}
	
}
