package Model;

public class Turtle extends Tank {
    private int age;
    public int getAge(){return age;}
    public void setAge(int newAge){ age = newAge;}

    public Turtle(int age)
    {
        this.age = age;
    }

    @Override
    public boolean checkAge() {
        return this.age >1;
    }

    public String toString()
    {
        return " " + age;
    }

}
