package View;

import Model.Fish;
import Model.Tank;
import Model.Turtle;
import Repository.IRepo;
import Controller.Controller;

public class MyView {
    public static void main(String args[])
    {
        IRepo r = new Repository.Repo(5);
        Controller c = new Controller(r);

        Fish f1 = new Fish(3);
        Fish f2 = new Fish(1);
        Turtle t1 = new Turtle(2);
        Turtle t2 = new Turtle(100);

        c.add(f1);
        c.add(f2);
        c.add(t1);
        c.add(t2);
        c.add(t2);


        //c.delete(0);
        //Tank[] k = c.getRepo();

        Tank[] aux = c.filter();
        for (Tank t: aux)
        {
            if(t != null)
            {
                System.out.println(t);
            }

        }


    }
}
