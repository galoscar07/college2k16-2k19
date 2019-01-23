package model.statements;

import model.ProgramState;
import model.containers.Dictionary;
import model.containers.ExecStack;
import model.containers.IDictionary;
import model.containers.IExecStack;

public class ForkStatement implements Statement {
    Statement st;

    public ForkStatement(Statement s){
        st = s;
    }

    @Override
    public ProgramState execute(ProgramState ps) {
        IExecStack<Statement> exec = new ExecStack<>();
        exec.push(st);
        IDictionary<String,Integer> symbols = new Dictionary<>();
        symbols.copy(ps.getSymbolTable());
        ProgramState clone = new ProgramState(ps.getId()*10,exec,symbols,ps.getList(),ps.getFileTable(),ps.getHeap());
        return clone;
    }
    public String toString(){
        return "fork("+this.st+")";
    }
}
