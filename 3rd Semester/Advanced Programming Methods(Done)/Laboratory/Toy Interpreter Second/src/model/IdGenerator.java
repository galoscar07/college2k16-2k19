package model;

public class IdGenerator {
    private static int a = 1;

    public static int generateId() {
        int b = a;
        a++;
        return b;
    }
}
