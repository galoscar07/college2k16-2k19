package Controller;
import Exceptions.*;
import Model.*;
import Model.Statements.IStmt;
import Model.Utils.*;
import Repo.IRepo;
import View.GUI.PrgListController;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Ctrl {
    private IRepo repo;
    private ExecutorService executor;

    public void addProgram(PrgState st){
        repo.addPrg(st);
    }

    private Map<Integer, Integer> conservativeGarbageCollector(Collection<Integer> symTbl, Map<Integer, Integer> heap)
    {
        return heap.entrySet().stream().filter(e->symTbl.contains(e.getKey())).collect(Collectors.toMap(Map.Entry::getKey,
                Map.Entry::getValue));
    }

    public Ctrl(){}

    public Ctrl(IRepo r){repo=r;}

    private List<PrgState> removeCompletedPrg(List<PrgState> inPrgList) {
        return inPrgList.stream()
                .filter(p -> p.isNotCompleted())
                .collect(Collectors.toList());
    }


    public IRepo getRepo(){return this.repo;}


    private void oneStepForAllPrg(List<PrgState> prgList) throws InterruptedException {
        prgList.forEach(prg ->repo.logPrgStateExec(prg));


        List<Callable<PrgState>> callList = prgList.stream()
                .map((PrgState p) -> (Callable<PrgState>)(() -> p.oneStep()))
                .collect(Collectors.toList());


        List<PrgState> newPrgList = executor.invokeAll(callList). stream()
                . map(future -> {
                    try {
                        return future.get();
                    } catch (Exception e) {
                        System.out.println("\n!!!Empty Stack!!!");
                        return null;
                    }
                })
                .filter(p -> p!=null)
                .collect(Collectors.toList());
        prgList.addAll(newPrgList);

        prgList.forEach(prg ->repo.logPrgStateExec(prg));
        prgList.forEach(prg->System.out.println(prg.toString()));
        repo.setPrgList(prgList);

    }


    public void allStep() throws InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        List<PrgState> prgList=removeCompletedPrg(repo.getPrgList());
        MyIList<Integer> out=new MyList<>();
        MyIHeap<Integer> heap=new MyHeap<>();
        while(prgList.size() > 0){

           Collection <Integer> symValues = new ArrayList<>();
            repo.getPrgList().forEach(e->symValues.addAll(e.getSymTable().getContent().values()));
            out=prgList.get(0).getOut();
            heap.setHeap(conservativeGarbageCollector(symValues,prgList.get(0).
                    getHeap().getContent()));
            oneStepForAllPrg(prgList);
            prgList = removeCompletedPrg(repo.getPrgList());
        }
        repo.CloseFile();
        executor.shutdownNow();
        repo.setPrgList(prgList);
        System.out.println(out.toString());
        System.out.println(heap.toString());
        System.out.println("End of program.");
    }

    public void allStepGUI() throws MyException {
        executor = Executors.newFixedThreadPool(2);
        List<PrgState> prgList = removeCompletedPrg(repo.getPrgList());
        if(prgList.size() == 0) {
            executor.shutdownNow();
            throw new MyException("Program finished.");
        }
        else {
            try {
                oneStepForAllPrg(prgList);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            executor.shutdownNow();
        }
    }
    public String toString() {
        return repo.getPrgList().get(0).getOriginalProgram().toString();
    }

}


