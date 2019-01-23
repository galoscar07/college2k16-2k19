package Model.Statements;

import Exceptions.MyControllerException;
import Model.PrgState;

public class Skip implements IStmt{

    public PrgState execute(PrgState state) throws MyControllerException {
        return null;
    }
}
