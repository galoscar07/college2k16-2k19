package model;

import model.containers.IDictionary;
import model.containers.IExecStack;
import model.containers.IHeap;
import model.containers.IList;
import model.exceptions.StatementException;
import model.statements.Statement;

import java.io.BufferedReader;

public class ProgramState {
    private IExecStack<Statement> execStack;
    private IDictionary<String, Integer> symbolT;
    private IList<Integer> messages;
    private IDictionary<Integer, Tuple<String, BufferedReader>> fileT;
    private IHeap<Integer, Integer> heap;
    private int id;

    public ProgramState(int i,IExecStack<Statement> es, IDictionary<String, Integer> st, IList<Integer> m, IDictionary<Integer, Tuple<String, BufferedReader>> ft, IHeap<Integer, Integer> h) {
        execStack = es;
        symbolT = st;
        id = i;
        messages = m;
        fileT = ft;
        heap = h;
    }

    public IDictionary<String, Integer> getSymbolTable() {
        return symbolT;
    }

    public void setSymbolTable(IDictionary<String, Integer> s) {
        symbolT=s;
    }

    public IExecStack<Statement> getExecStack() {
        return execStack;
    }

    public void setExecStack(IExecStack<Statement> e) {
        execStack = e;
    }

    public IList<Integer> getList() {
        return messages;
    }

    public void setList(IList<Integer> l) {
        messages = l;
    }

    public IDictionary<Integer, Tuple<String, BufferedReader>> getFileTable() {
        return fileT;
    }

    public void setFileTable(IDictionary<Integer, Tuple<String, BufferedReader>> f)
    {
        fileT=f;
    }

    public IHeap<Integer, Integer> getHeap() {
        return heap;
    }

    public void getHeap(IHeap<Integer, Integer> h) {
        heap = h;
    }

    public int getId(){
        return id;
    }

    public void setId(int i){
        id = i;
    }

    public Boolean isNotCompleted(){
        return !execStack.isEmpty();
    }

    public ProgramState executeOneStep() {
        if (execStack.isEmpty()) {
            throw new StatementException("Execution stack is empty");
        }
        Statement st = execStack.pop();
        return st.execute(this);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(">>>>>\n");
        sb.append("ID: ").append(id).append("\n");
        if (!execStack.toString().isEmpty()) {
            sb.append("Execution Stack: \n").append(execStack);
        }
        if (!symbolT.toString().isEmpty()) {
            sb.append("Symbol Table: \n").append(symbolT);
        }
        if (!messages.toString().isEmpty()) {
            sb.append("Screen: \n").append(messages);
        }
        if (!fileT.toString().isEmpty()) {
            sb.append("File Table: \n").append(fileT);
        }

        if (!heap.toString().isEmpty()) {
            sb.append("Heap: \n").append(heap);
        }
        sb.append(">>>>>");
        return sb.toString();
    }
}
