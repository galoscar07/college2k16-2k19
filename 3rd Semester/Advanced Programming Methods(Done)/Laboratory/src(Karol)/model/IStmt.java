package model;

import exception.*;

import java.io.IOException;

public interface IStmt{
    @Override
    String toString();
    PrgState execute(PrgState state) throws IOException, FileAlreadyOpenedException, FileNotOpenedException, UnknownVariableException, DivideByZeroException, UnknownComparisonExpression, IOException, UnknownComparisonExpression;
}
