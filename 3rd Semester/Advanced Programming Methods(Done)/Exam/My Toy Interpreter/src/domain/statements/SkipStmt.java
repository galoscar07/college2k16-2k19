package domain.statements;

import domain.PrgState;

public class SkipStmt implements IStmt{

    public PrgState execute(PrgState state){
        return null;
    }
}
