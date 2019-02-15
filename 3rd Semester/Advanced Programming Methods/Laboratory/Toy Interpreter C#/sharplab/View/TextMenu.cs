using sharplab.View.Commands;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace sharplab.View
{
    class TextMenu
    {
        private IDictionary<string, Command> commands;
        public TextMenu() { commands = new Dictionary<string,Command>(); }
        public void AddCommand(Command c) { commands.Add(c.GetName(), c); }
        private void PrintMenu()
        {
            foreach (Command com in commands.Values.ToArray())
            {
                string line = com.GetName() + "." + com.GetDescription();
                Console.WriteLine(line);
            }
        }

        public void Show()
        {
            while (true)
            {
                PrintMenu();
                System.Console.WriteLine("Choose option: ");
                String key = System.Console.ReadLine();
                Command com = commands[key];
                if (com == null)
                {
                    System.Console.WriteLine("Invalid option!");
                    continue;
                }
                com.Execute();
            }
        }

    }
}
