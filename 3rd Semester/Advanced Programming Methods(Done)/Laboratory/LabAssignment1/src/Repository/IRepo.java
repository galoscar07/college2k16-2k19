package Repository;

import Model.MyException;
import Model.Tank;

public interface IRepo {
    public void Add(Model.Tank t) throws MyException;
    public void Delete(int pos) throws MyException;
    public Model.Tank[] Filter();
    public Tank[] getTank();


}
