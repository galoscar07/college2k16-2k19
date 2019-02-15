package exception;

public class FileNotOpenedException extends Exception {
    public FileNotOpenedException() {
        super("FileNotOpenedException");
    }
    public FileNotOpenedException(String s) {
        super(s);
    }
}
