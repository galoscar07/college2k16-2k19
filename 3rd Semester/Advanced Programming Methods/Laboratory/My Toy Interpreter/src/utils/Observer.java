package utils;

public interface Observer <T> {
    void update(Observable<T> observable);
}
