package view;

public class ExitCommand extends Command {
    public ExitCommand(String key, String descr) {
        super(key, descr);
    }

    @Override
    public void execute() {
        System.out.println("Bye bye!");
        System.exit(0);
    }
}
