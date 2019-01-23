package controller;

import model.ProgramState;
import model.Tuple;
import model.containers.IDictionary;
import model.containers.IExecStack;
import model.containers.IHeap;
import model.statements.Statement;
import repository.IProgramStateRepository;

import java.io.BufferedReader;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class Controller {
    private IProgramStateRepository repository;

    public Controller(IProgramStateRepository r) {
        repository = r;
    }

    public void executeOneStep() {
        ProgramState ps = repository.getCurrentProgram();
        IExecStack<Statement> es = ps.getExecStack();
        if (!es.isEmpty()) {
            Statement st = es.pop();
            st.execute(ps);
            System.out.println(ps);
        }
    }

    private void closeAllFiles(IDictionary<Integer, Tuple<String, BufferedReader>> fileT) {
        fileT.toArrayList().stream().map(e -> e.getValue().y).forEach(a -> {
            try {
                if (a != null && a.ready())
                    a.close();
            } catch (java.io.IOException ignored) {
            }
        });
        fileT.empty();
    }

    private Map<Integer, Integer> conservativeGarbageCollector(Collection<Integer> symTableValues, Map<Integer, Integer> heap) {
        return heap.entrySet().stream()
                .filter(m -> symTableValues.contains(m.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public void executeAll() {
        ProgramState ps = repository.getCurrentProgram();
        try {
            IExecStack<Statement> es = ps.getExecStack();
            while (!es.isEmpty()) {
                Statement st = es.pop();
                st.execute(ps);
                IHeap<Integer, Integer> h = ps.getHeap();
                IDictionary<String, Integer> symT = ps.getSymbolTable();
                Map<Integer, Integer> r = conservativeGarbageCollector(symT.getContent().values(), h.getContent());
                h.setContent(r);
                System.out.println(ps);
                repository.logProgramStateExec();
                //System.out.println(ps.getFileTable());
            }
        } finally {
            closeAllFiles(ps.getFileTable());
            System.out.println("File table: "+ps.getFileTable());
        }
    }
}