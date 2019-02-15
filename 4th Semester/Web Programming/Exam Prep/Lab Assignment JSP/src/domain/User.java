package domain;

public class User {
    private int id;
    private String username;
    private String password;

    public User(int id, String userName, String password)
    {
        this.id = id;
        this.username = userName;
        this.password = password;
    }

    public int getId() {
        return id;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
