package view;

import controller.Controller;
import model.exceptions.MyException;

public class RunExampleCommand extends Command {
    private Controller ctr;

    RunExampleCommand(String key, String desc, Controller ctr) {
        super(key, desc);
        this.ctr = ctr;
    }

    @Override
    public void execute() {
        try {
            ctr.executeAll();
        } catch (MyException e) {
            System.out.println(e.getMessage());
        }
    }
}
