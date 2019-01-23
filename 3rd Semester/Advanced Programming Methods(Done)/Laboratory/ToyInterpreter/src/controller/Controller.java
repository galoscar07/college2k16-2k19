package controller;

import javafx.util.Pair;
import model.ProgramState;
import model.Tuple;
import model.containers.IDictionary;
import model.containers.IExecStack;
import model.containers.IHeap;
import model.exceptions.ControllerException;
import model.statements.Statement;
import repository.IProgramStateRepository;

import java.io.BufferedReader;
import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Controller {
    private IProgramStateRepository repository;
    private ExecutorService executor;

    public Controller(IProgramStateRepository r) {
        repository = r;
    }

    private List<ProgramState> removeCompleted(List<ProgramState> list) {
        return list.stream()
                .filter(ProgramState::isNotCompleted)
                .collect(Collectors.toList());
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

    public void add(ProgramState prgState) {
        repository.addProgramState(prgState);
    }

    private void oneStepForAll(List<ProgramState> list){
        List<Callable<ProgramState>> callList = list.stream()
                .map((ProgramState p) -> (Callable<ProgramState>) (p::executeOneStep))
                .collect(Collectors.toList());
        try {
            List<ProgramState> newPrgList = executor.invokeAll(callList)
                    .stream()
                    .map(future -> {
                        try {
                            return future.get();
                        } catch (InterruptedException | ExecutionException e) {
                            throw new ControllerException("Execution stopped");
                        }
                    })
                    .filter(Objects::nonNull)
                    .collect(Collectors.toList());
            list.addAll(newPrgList);
        } catch (InterruptedException e) {
            throw new ControllerException("InterruptedException");
        }
        list.forEach(repository::logProgramStateExec);
        repository.setProgramList(list);
    }

    private Map<Integer, Integer> conservativeGarbageCollector(List<ProgramState> list) {
        return list.get(0).getHeap().getContent().entrySet().stream()
                .filter(e -> {
                            for (ProgramState prgState : list) {
                                if (prgState.getSymbolTable().getContent().values().contains(e.getKey()))
                                    return true;
                            }
                            return false;
                        }
                )
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public void executeAll() {
        List<ProgramState> list = removeCompleted(repository.getProgramList());
        if ( list.size() == 0)
        {
            throw new ControllerException("Nothing to execute");
        }
        executor = Executors.newFixedThreadPool(2);
        IDictionary<Integer,Tuple<String,BufferedReader>> fileITable = list.get(0).getFileTable();
        while (list.size() > 0) {
            IHeap<Integer, Integer> heap = list.get(0).getHeap();
            heap.setContent(conservativeGarbageCollector(list));
            oneStepForAll(list);
            for(int i=0;i<list.size();i++){
                System.out.println(list.get(i));
            }
            list = removeCompleted(list);
        }
        executor.shutdownNow();
        closeAllFiles(fileITable);
        repository.setProgramList(list);
    }
}