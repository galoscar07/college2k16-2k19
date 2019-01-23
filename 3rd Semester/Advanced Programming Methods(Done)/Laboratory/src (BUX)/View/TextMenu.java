package View;

import View.Commands.Command;

import java.util.*;


public class TextMenu
{
    private Map<String, Command> commands;
    public TextMenu(){commands = new HashMap<>();}
    public void addCommand(Command c){commands.put(c.getKey(),c);}
    private void printMenu()
    {
        for(Command com:commands.values())
        {
            String line = String.format("%4s: %s", com.getKey(), com.getDescription());
            System.out.println(line);
        }
    }

    public void show()
    {
        Scanner scanner = new Scanner(System.in);
        while(true)
        {
            printMenu();
            System.out.println("Choose option: ");
            String key = scanner.nextLine();
            Command com = commands.get(key);
            if(com == null)
            {
                System.out.println("Invalid option!");
                continue;
            }
            com.execute();
        }
    }

}
