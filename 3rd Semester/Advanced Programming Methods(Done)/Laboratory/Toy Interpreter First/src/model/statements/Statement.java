package model.statements;

import model.ProgramState;

public interface Statement {
    ProgramState execute(ProgramState ps);
}
