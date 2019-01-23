package model.statements;

import model.ProgramState;
import model.containers.Dictionary;
import model.containers.ExecStack;
import model.containers.IDictionary;
import model.containers.IExecStack;

import java.util.Random;

public class ForkStatement implements Statement {
    private Statement st;

    public ForkStatement(Statement s){
        st = s;
    }

    @Override
    public ProgramState execute(ProgramState ps) {
        IExecStack<Statement> exec = new ExecStack<>();
        exec.push(st);
        IDictionary<String,Integer> symbols = ps.getSymbolTable().getCopy();
        return new ProgramState(ps.getId()* new Random().nextInt(100),exec,symbols,ps.getList(),ps.getFileTable(),ps.getHeap());
    }

    @Override
    public String toString() {
        return "fork("+st+")";
    }
}
