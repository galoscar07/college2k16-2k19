package Model.Statements;

import Exceptions.MyControllerException;
import Exceptions.MyDictionaryException;
import Model.PrgState;


public interface IStmt {

    public PrgState execute(PrgState state) throws MyControllerException, MyDictionaryException;

    String toString();
}
