package Controller;

import Model.MyException;
import Model.Tank;
import Repository.IRepo;

public class Controller {
    IRepo repo;
    public Controller (IRepo r)
    {
        repo = r;
    }

    public void add(Model.Tank t)
    {
        try {repo.Add(t);}
        catch (MyException e) {
            System.out.print("Index out of range!\n");
        }
    }

    public void delete(int pos)
    {
        try {repo.Delete(pos);}
        catch (MyException e)
        {
            System.out.print("Index out of range~ \n");
        }
    }
    public Tank[] filter()
    {
        return repo.Filter();
    }

    public Tank[] getRepo()
    {
        return repo.getTank();
    }

}
