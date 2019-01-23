package View.Commands;

import Controller.Ctrl;
import Exceptions.MyViewException;

public class RunCommand extends Command
{
    private Ctrl ctr;
    public RunCommand(String key, String desc, Ctrl ctr)
    {
        super(key, desc);
        this.ctr = ctr;
    }
    public void execute() {
        try{
            ctr.allStep();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
