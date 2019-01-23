package ro.ubb.reflection;

import java.lang.reflect.Field;
import java.lang.reflect.Method;

/**
 * 1.
 * - create a new "ro.ubb.reflection.Student" instance (reflection).
 * - initialize the student's private attributes ("name", "groupNumber") with the values ("john", 123).
 * - print the student instance.
 * <p>
 * 2.
 * - create a new "ro.ubb.reflection.Student" instance (reflection)
 * - invoke setName("john") and setGroupNumber(123)
 * - print the student instance.
 * <p>
 * 3.
 * - create a new "ro.ubb.reflection.Student" instance ("john",123) by invoking the constructor
 * - print the student instance.
 * <p>
 * 4.
 * - create a new "ro.ubb.reflection.Employee". ("ro.ubb.reflection.e04.Employee" extends "ro.ubb.reflection.Person", Person has a
 * name, Employee has a salary) (reflection)
 * - set the "name" to "Mary" and the "salary" to 1000;
 * - print the employee
 * <p>
 * 5.
 * - given a Student instance ("John",123), print all attribute names, types, and values.
 */
public class Main {


    public static void main(String[] args) throws Exception {
//        problem1();
        //problem2();
        //problem3();
//        problem4();
        problem5();
    }

    private static void problem5() throws IllegalAccessException {
        Student student=new Student("john",123);
        Field[] fields=student.getClass().getDeclaredFields();
        for(Field f:fields){
            f.setAccessible(true);
            System.out.println(f.getName()+" "+f.getType()+" "+f.get(student));
        }
    }

    private static void problem4() throws Exception {
        Employee e = (Employee)Class
                .forName("ro.ubb.reflection.Employee")
                .getDeclaredConstructor()
                .newInstance();
        Field nameField = e.getClass().getSuperclass()
                .getDeclaredField("name");
        nameField.setAccessible(true);
        nameField.set(e,"Mary");

        Field salaryField = e.getClass()
                .getDeclaredField("salary");
        salaryField.setAccessible(true);
        salaryField.set(e,1000);

        System.out.println(e);

    }

    private static void problem3() throws Exception {
        Student s = (Student)Class
                .forName("ro.ubb.reflection.Student")
                .getDeclaredConstructor(String.class, int.class)
                .newInstance("John", 123);

        System.out.println(s);
    }

    private static void problem2() throws Exception{
        Student s=(Student)Class.forName("ro.ubb.reflection.Student")
                .getDeclaredConstructor()
                .newInstance();
        Method setNameMethod = s.getClass().getDeclaredMethod("setName",String.class);
        Method setGroupMethod = s.getClass().getDeclaredMethod("setGroup", int.class);
        setNameMethod.invoke(s, "Joe");
        setGroupMethod.invoke(s, 321);
        System.out.println(s);
    }

    private static void problem1() throws InstantiationException, IllegalAccessException, java.lang.reflect.InvocationTargetException, NoSuchMethodException, ClassNotFoundException, NoSuchFieldException {
        Student s=(Student)Class.forName("ro.ubb.reflection.Student")
                .getDeclaredConstructor()
                .newInstance();
        Field nameField = s.getClass()
                .getDeclaredField("name");
        nameField.setAccessible(true);
        nameField.set(s,"john");
        Field groupField = s.getClass()
                .getDeclaredField("group");
        groupField.setAccessible(true);
        groupField.setInt(s,123);
        System.out.println(s);
    }
}



