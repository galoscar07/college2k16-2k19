package Repository;

import Model.MyException;
import Model.Tank;

public class Repo implements IRepo {
    private Tank[] FishTank;
    private int currentPos =0 ;

    public Repo(int len)
    {
        FishTank = new Tank[len];
    }

    @Override
    public void Add(Tank t) throws MyException{
        if(FishTank.length <= currentPos )
            throw new MyException();
        FishTank[currentPos] = t;
        currentPos++;

    }

    @Override
    public void Delete(int pos) throws MyException {
        if(pos >= currentPos)
        {
            throw new MyException();

        }

        for( int i = pos; i < FishTank.length -1 ; i++)
        {
            FishTank[i] = FishTank[i+1];
        }
        FishTank[FishTank.length -1] = null;
    }

    @Override
    public Tank[] Filter() {
        Tank[] filterTank = new Tank[FishTank.length];
        int i = 0;
        for(Tank t: FishTank)
        {
            if(t != null && t.checkAge()) {
                filterTank[i] = t;
                i++;
            }
        }
        return filterTank;
    }

    public Tank[] getTank()
    {
        return this.FishTank;
    }
}
