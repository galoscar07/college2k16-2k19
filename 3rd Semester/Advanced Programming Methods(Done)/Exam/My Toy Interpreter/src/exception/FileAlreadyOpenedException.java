package exception;

public class FileAlreadyOpenedException extends Exception {
    public FileAlreadyOpenedException() {
        super("FileAlreadyOpenedException");
    }
    public FileAlreadyOpenedException(String s) {
        super(s);
    }
}
