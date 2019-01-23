package ro.ubb.reflection;

public class Employee extends Person {
    private int salary;

    public Employee() {}

    public Employee(String name, int sal) {
        super(name);
        this.salary = sal;
    }

    @Override
    public String toString() {
        return "Employee{" +
                "salary=" + salary +
                "} " + super.toString();
    }
}
